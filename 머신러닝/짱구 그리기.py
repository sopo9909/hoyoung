<<<<<<< HEAD
#그림그리는것
import cv2, random, os, sys
import numpy as np
from copy import deepcopy
from skimage.measure import compare_mse
import multiprocessing as mp
filepath = '230px-신짱구.png'
img = cv2.imread(filepath)
height, width, channels = img.shape

n_initial_genes = 50
n_population = 50
prob_mutation = 0.01
prob_add =0.3
prob_remove = 0.2

min_radius, max_radius = 5,15
save_every_n_iter = 100

class Gene():
  def __init__(self):
    self.center = np.array([random.randint(0,width),random.randint(0,height)])
    self.radius = random.randint(min_radius,max_radius)
    self.color = np.array([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
  def mutate(self):
    mutation_size = max(1,int(round(random.gauss(15,4))))/100
    r = random.uniform(0,1)
    if r < 0.33:
      self.radius = np.clip(random.randint(int(self.radius*(1-mutation_size)),int(self.radius*(1+mutation_size))),1,100)
    elif r < 0.66:
      self.radius = np.array([np.clip(random.randint(int(self.center[0]*(1-mutation_size)),int(self.center[0]*(1+mutation_size))),0,width),np.clip(random.randint(int(self.center[1]*(1-mutation_size)),int(self.center[1]*(1+mutation_size))),0,height)])
    else:#color
      self.color = np.array([np.clip(random.randint(int(self.color[0]*(1-mutation_size)),int(self.color[0]*(1+mutation_size))),0,255)])
def compute_fitness(genome):
  out = np.ones((height,width,channels),dtype=np.uint8)*255
  for gene in genome:
    cv2.circle(out,center=tuple(gene.center),radius=gene.radius,color=(int(gene.color[0]),int(gene.color[1]),int(gene.color[2])),thickness=-1)
  fitness = 255./compare_mse(img,out)
  return fitness,out
def compute_population(g):
  genome = deepcopy(g)
  if len(genome)<200:
    for gene in genome:
      if random.uniform(0,1)<prob_mutation:
        gene.mutate()
  else:
    for gene in random.sample(genome,k=int(len(genome)*prob_mutation)):
      gene.mutate()
  if random.uniform(0,1)<prob_add:
    genome.append(Gene())
  if len(genome)>0 and random.uniform(0,1) < prob_remove:
    genome.remove(random.choice(genome))
  new_fitness,new_out = compute_fitness(genome)
  return new_fitness, genome, new_out
if __name__ == '__main__':
  os.makedirs('result',exist_ok=True)
  p = mp.Pool(mp.cpu_count()-1)
  best_genome =[Gene() for _ in range(n_initial_genes)]
  best_fitness, best_out = compute_fitness(best_genome)
  n_gen = 0
  
  while True:
    try:
      results = p.map(compute_population,[deepcopy(best_genome)]*n_population)
    except KeyboardInterrupt:
      p.close()
      break
    results.append([best_fitness,best_genome,best_out])
    new_fitness, new_genomes, new_out = zip(*results)
    best_result = sorted(zip(new_fitness,new_genomes,new_out),key=lambda x: x,reverse=True)
    best_fitness, best_genome, best_out = best_result[0]

    print('Generation #%s, Fitness %s' % (n_gen,best_fitness))
    n_gen += 1
    if n_gen % save_every_n_iter ==0:
      cv2.imwrite('result/%s_%s.jpg' % (filename,n_gen),best_out)
    cv2.imshow('best out', best_out)
    if cv2.waitKey(1) == ord('q'):
      p.close()
      break
    cv2.imshow('best out',best_out)
=======
#그림그리는것
import cv2, random, os, sys
import numpy as np
from copy import deepcopy
from skimage.measure import compare_mse
import multiprocessing as mp
filepath = '230px-신짱구.png'
img = cv2.imread(filepath)
height, width, channels = img.shape

n_initial_genes = 50
n_population = 50
prob_mutation = 0.01
prob_add =0.3
prob_remove = 0.2

min_radius, max_radius = 5,15
save_every_n_iter = 100

class Gene():
  def __init__(self):
    self.center = np.array([random.randint(0,width),random.randint(0,height)])
    self.radius = random.randint(min_radius,max_radius)
    self.color = np.array([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
  def mutate(self):
    mutation_size = max(1,int(round(random.gauss(15,4))))/100
    r = random.uniform(0,1)
    if r < 0.33:
      self.radius = np.clip(random.randint(int(self.radius*(1-mutation_size)),int(self.radius*(1+mutation_size))),1,100)
    elif r < 0.66:
      self.radius = np.array([np.clip(random.randint(int(self.center[0]*(1-mutation_size)),int(self.center[0]*(1+mutation_size))),0,width),np.clip(random.randint(int(self.center[1]*(1-mutation_size)),int(self.center[1]*(1+mutation_size))),0,height)])
    else:#color
      self.color = np.array([np.clip(random.randint(int(self.color[0]*(1-mutation_size)),int(self.color[0]*(1+mutation_size))),0,255)])
def compute_fitness(genome):
  out = np.ones((height,width,channels),dtype=np.uint8)*255
  for gene in genome:
    cv2.circle(out,center=tuple(gene.center),radius=gene.radius,color=(int(gene.color[0]),int(gene.color[1]),int(gene.color[2])),thickness=-1)
  fitness = 255./compare_mse(img,out)
  return fitness,out
def compute_population(g):
  genome = deepcopy(g)
  if len(genome)<200:
    for gene in genome:
      if random.uniform(0,1)<prob_mutation:
        gene.mutate()
  else:
    for gene in random.sample(genome,k=int(len(genome)*prob_mutation)):
      gene.mutate()
  if random.uniform(0,1)<prob_add:
    genome.append(Gene())
  if len(genome)>0 and random.uniform(0,1) < prob_remove:
    genome.remove(random.choice(genome))
  new_fitness,new_out = compute_fitness(genome)
  return new_fitness, genome, new_out
if __name__ == '__main__':
  os.makedirs('result',exist_ok=True)
  p = mp.Pool(mp.cpu_count()-1)
  best_genome =[Gene() for _ in range(n_initial_genes)]
  best_fitness, best_out = compute_fitness(best_genome)
  n_gen = 0
  
  while True:
    try:
      results = p.map(compute_population,[deepcopy(best_genome)]*n_population)
    except KeyboardInterrupt:
      p.close()
      break
    results.append([best_fitness,best_genome,best_out])
    new_fitness, new_genomes, new_out = zip(*results)
    best_result = sorted(zip(new_fitness,new_genomes,new_out),key=lambda x: x,reverse=True)
    best_fitness, best_genome, best_out = best_result[0]

    print('Generation #%s, Fitness %s' % (n_gen,best_fitness))
    n_gen += 1
    if n_gen % save_every_n_iter ==0:
      cv2.imwrite('result/%s_%s.jpg' % (filename,n_gen),best_out)
    cv2.imshow('best out', best_out)
    if cv2.waitKey(1) == ord('q'):
      p.close()
      break
    cv2.imshow('best out',best_out)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
    cv2.waitKey(0)