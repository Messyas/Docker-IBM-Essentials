# Inicializa o Swarm no nó manager, anunciando o endereço eth0 para os outros nós
docker swarm init --advertise-addr eth0

# Junta este nó ao Swarm como worker, usando o token gerado e o endereço do manager
docker swarm join --token SWMTKN-1-50qba7hmo5exuapkmrj6jki8knfvinceo68xjmh322y7c8f0pj-87mjqjho30uue43oqbhhthjui 10.0.120.3:2377

# Exibe o comando e token necessários para adicionar um manager ao Swarm
docker swarm join-token manager

# Lista todos os nós do Swarm, mostrando hostname, status e papel (manager/worker)
docker node ls

# etapa 2

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

# etapa 3

# Exibe os logs agregados do serviço “nginx1” sem truncar as mensagens
docker service logs nginx1 --no-trunc

# Atualiza o serviço “nginx1” para ter 5 réplicas, executando em segundo plano
docker service update --replicas=5 --detach=true nginx1

# Lista as tarefas (containers) do serviço “nginx1” e seus estados atuais
docker service ps nginx1

# Envia uma requisição HTTP para localhost:80, exibindo o hostname do nó que atendeu
curl localhost:80

# Repita a chamada curl para observar o balanceamento entre nós
curl localhost:80
curl localhost:80
curl localhost:80

# Exibe novamente os logs agregados do serviço para ver qual container/nó atendeu cada requisição
docker service logs nginx1

# etapa 4

# Inicia o rolling update do serviço “nginx1” para usar a imagem nginx:1.13
docker service update --image nginx:1.13 --detach=true nginx1

# Monitora o progresso das tasks para ver os containers sendo atualizados
docker service ps nginx1

# etapa 5

# Cria um novo serviço “nginx2” com 5 réplicas, publica a porta 81 no host para a porta 80 do container e monta o hostname do nó em index.html
docker service create --detach=true --name nginx2 --replicas=5 --publish 81:80 \
  --mount type=bind,source=/etc/hostname,target=/usr/share/nginx/html/index.html,ro \
  nginx:1.12

# Monitora em tempo real (a cada 1s) o estado das tasks do serviço “nginx2”
watch -n 1 docker service ps nginx2

# Faz o nó atual deixar o swarm
docker swarm leave

# Notes importantes 
# 6. Determine how many nodes you need

🔹 Configuração do Cluster
Um cluster com 1 gerente + 2 workers não é altamente disponível.

Se o nó gerente cair, o cluster para de funcionar.

🔹 Alta Disponibilidade
Para produção, é recomendado múltiplos nós gerentes.

Recomendação:

3 nós gerentes toleram 1 falha.

5 nós gerentes toleram 2 falhas.

7 nós gerentes toleram 3 falhas.

Ter número par de nós gerentes não aumenta a tolerância a falhas.

🔹 Algoritmo Raft
O cluster usa consenso Raft.

É necessário mais de 50% dos gerentes ativos para funcionar.

🔹 Nós Workers
Podem ser milhares, diferente dos gerentes.

Usam o protocolo gossip para comunicação eficiente em larga escala.