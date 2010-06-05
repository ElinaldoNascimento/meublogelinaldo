from django.db import models

class Artigo (models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField()
    #sobrenome = models.CharField(max_length=100)
    autor = models.ForeignKey('Autor')
    #autor = models.ManyToManyField('Autor')
    
        
    def __unicode__(self):
        
        return self.titulo
    
class Autor (models.Model):
    
    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=40)
    cep = models.IntegerField()
    email = models.EmailField()
    
    def __unicode__(self): # esta funcao define q atributo do objeto sera impresso qndo o objeto for chamado
        return self.nome
    

