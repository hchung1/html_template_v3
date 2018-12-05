from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.query import Every
from whoosh import writing
import os, ast, shutil


def start_whoosh():
  if os.path.exists("whoosh_file"):
    shutil.rmtree("whoosh_file")
  os.mkdir("whoosh_file")
  home = os.getcwd()
  schema = Schema(table_name=TEXT(stored=True), view_type=TEXT(stored=True), name=TEXT(stored=True))
  ix = create_in("whoosh_file", schema)
  writer = ix.writer()
  for i in os.walk(home):
    topic = ((i[0].split("/")[::-1])[0])
    if topic == "templates":
      os.chdir(i[0])
      html = os.listdir()
      os.chdir(home)
      for x in range(len(html)):
        temp = (html[x].split("."))[0].split("_")
        writer.add_document(table_name=temp[0], view_type=temp[1], name=temp[2])
  writer.commit()
  return True


def create_view(apps):
  ix = open_dir("whoosh_file")
  result = list(ix.searcher().search(Every('table_name')))
  f = open(apps+"/views.py","w")
  f.write("from django.shortcuts import render\nfrom django.views import generic\nfrom .models import *\n\n")
  for i in range(len(result)):
    d = ast.literal_eval(str(result[i])[5:][:-1])
    if d['view_type']=='base':
      b = "ListView"
    if d['view_type']=='list':
      b = "DetailView"
    if d['name'] == 'home':
      f.write("class HomeView (generic." + b + "):\n    model=" + d['table_name']  + "\n    template_name =\""+ d['table_name']  + "_" + d['view_type'] + "_" + d['name'] + ".html\"\n\n\n")
    if d['name'] != 'home':
      f.write("class "+ d['table_name'] + d['name'] + b + " (generic." + b + "):\n    model=" + d['table_name']  + "\n    template_name =\""+ d['table_name']  + "_" + d['view_type'] + "_" + d['name'] + ".html\"\n\n\n")
  f.close()


def create_urls(url_folder, apps):
  ix = open_dir("whoosh_file")
  result = list(ix.searcher().search(Every('table_name')))
  f = open(url_folder+"/urls.py","w")
  f.write("from django.contrib import admin\nfrom django.urls import path\nfrom "+apps+".views import *\n\nurlpatterns=[\npath('admin/', admin.site.urls),\n")
  for i in range(len(result)):
    d = ast.literal_eval(str(result[i])[5:][:-1])
    if d['view_type']=='base':
      b = "ListView"
      c = "/"
    if d['view_type']=='list':
      b = "DetailView"
      c="/<int:pk>/"
    if d['name'] == 'home':
      f.write("path('',HomeView.as_view(),name=\""+d['name']+"\"),\n")
    if d['name'] != 'home':
      f.write("path('"+ d['name'] + c +"'," + d['table_name'] + d['name'] + b + ".as_view(),name=\""+d['name']+"\"),\n")
  f.write("]")
  f.close()

