# Inicializa o Swarm no nó manager, anunciando o endereço eth0 para os outros nós
docker swarm init --advertise-addr eth0

# Junta este nó ao Swarm como worker, usando o token gerado e o endereço do manager
docker swarm join --token SWMTKN-1-50qba7hmo5exuapkmrj6jki8knfvinceo68xjmh322y7c8f0pj-87mjqjho30uue43oqbhhthjui 10.0.120.3:2377

# Exibe o comando e token necessários para adicionar um manager ao Swarm
docker swarm join-token manager

# Lista todos os nós do Swarm, mostrando hostname, status e papel (manager/worker)
docker node ls

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
