import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def sort_dict(seq):
    dict1 = seq
    sorted_values = reversed(sorted(dict1.values()))
    sorted_dict = {}
    for i in sorted_values:
      for k in dict1.keys():
        if dict1[k] == i:
          sorted_dict[k] = dict1[k]
    return sorted_dict

def country_count(seq):
      dict_count = {}
      for i in seq:
          dict_count[i] = seq.count(i)
      return dict_count

def cleaner(seq):
    str2 = []
    for i in seq:
      if i.find(',') == -1:
        str2.append(i)
      else:
        str2.append(i.replace(',',''))
    return str2

def flatten(s):
    a = []
    for i in s:
      if type(i) is str:
        a.append(i)
      else:
        a.extend(flatten(i))
    return a

def list_country(tab):
    str1 = []
    for i in tab:
      if type(i) is int:
        continue
      elif type(i) is str:
        if i.find(',') == -1:
          str1.append(i)
        else:
          str1.append(i.split(', '))
    return str1

def year_list(l,k):
  y_list = []
  for i in l[k]:
    y_list.append(i)
  return y_list

def type_list(l,k):
  t_list = []
  for i in l[k]:
    t_list.append(i)
  return t_list 

def summovie(type,year):
  summovie = 0  
  for t, y in zip(type, year):
    if t == 'Movie' and y > 2001:
      summovie +=1
  return summovie  

def sumtvshow (type,year):
  sumtvshow = 0  
  for t, y in zip(type, year):
    if t == 'TV Show' and y > 2001:
      sumtvshow +=1
  return sumtvshow  


def t1():
  tab = pd.read_csv('netflix_titles.csv')

  types = type_list(tab, 'type')
  years = year_list(tab, 'release_year')

  labels = ['G1']
  movie = [summovie(types,years)]
  women_means = [sumtvshow(types,years)]

  x = np.arange(len(labels)) 
  width = 0.35  

  fig, ax = plt.subplots()
  rects1 = ax.bar(x - width/2, movie, width, label='Movie')
  rects2 = ax.bar(x + width/2, women_means, width, label='TV Shows')

  ax.set_ylabel('Quantity for 20 years')
  ax.set_title('Comparison of movies and TV Shows')
  ax.set_xticks(x)
  ax.set_xticklabels(labels)
  ax.legend()

  ax.bar_label(rects1, padding=3)
  ax.bar_label(rects2, padding=3)

  fig.tight_layout()

  plt.show()


def t2():
  tab = pd.read_csv('netflix_titles.csv')
  tab = tab['country']

  top_dict = sort_dict(country_count(cleaner(flatten(list_country(tab)))))

  top_country = list(top_dict)
  top_country = top_country[0:10]
  top_country.append('Others')
  count_release = list(top_dict.values())
  sum_count_release = sum(count_release[10:])
  count_release = count_release[0:10]
  count_release.append(sum_count_release)


  labels = top_country
  sizes = count_release
  explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
          shadow=True, startangle=110)
  ax1.axis('equal') 

  plt.show()


def t3():
  tab = pd.read_csv('netflix_titles.csv')
  tab = tab['listed_in']
  years = year_list(tab, 'release_year')
  
  def pop_genere(gen,year):
    genere = []  
    for g, y in zip(gen, year):
      if  y > 2011:
        genere.append(g)
    return genere  

  top_dict = sort_dict(country_count(cleaner(flatten(pop_genere(list_country(tab),years)))))

  top_genre = list(top_dict)
  top_genre = top_genre[0:20]
  count_release = list(top_dict.values())
  count_release = count_release[0:20]


  plt.rcdefaults()
  fig, ax = plt.subplots()

  # Example data
  genre = top_genre
  y_pos = np.arange(len(genre))
  performance = count_release
  error = np.random.rand(len(genre))

  ax.barh(y_pos, performance, xerr=error, align='center')
  ax.set_yticks(y_pos)
  ax.set_yticklabels(genre)
  ax.invert_yaxis()
  ax.set_xlabel('Performance')
  ax.set_title('The most popular genres')

  plt.show()