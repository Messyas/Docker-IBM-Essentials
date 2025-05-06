# Cria um serviço “nginx1” no Swarm, publica a porta 80 e monta o hostname do nó no index.html
docker service create --detach=true --name nginx1 --publish 80:80 \
  --mount source=/etc/hostname,target=/usr/share/nginx/html/index.html,type=bind,ro \
  nginx:1.12 pgqdxr41dpy8qwkn6qm7vke0q

# Lista todos os serviços em execução no Swarm
docker service ls

# Exibe as tarefas (containers) associadas ao serviço “nginx1” e seus estados
docker service ps nginx1

# Lista os containers em execução no nó atual
docker container ls

# Testa o serviço HTTP na porta 80, mostrando o hostname do nó que atendeu
curl localhost:80
