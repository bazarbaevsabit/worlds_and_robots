🎨 Color Follower (ROS2 + Gazebo)

Робот едет вдоль цветных кубов и выводит название распознанного цвета в консоль.

- Ubuntu 24.04  
- ROS2 Jazzy  
- Gazebo Harmonic  
- Docker

 🚀 Быстрый старт

Способ 1: Docker (рекомендуемый)


git clone https://github.com/bazarbaevssabit/color-follower-ros2.git
cd color-follower-ros2
chmod +x run.sh
./run.sh


После запуска ты окажешься внутри контейнера в папке `/home/work/project_w`.

Далее внутри контейнера:


ros2 launch mobile launch.py


Способ 2: без Docker (нативно)

cd ~/color-follower-ros2/src/mobile
colcon build
source install/setup.bash
ros2 launch mobile launch.py


📁 Что здесь

- `run.sh` – скрипт для запуска Docker-контейнера с пробросом графики
	внутри данного файла необходимо изменить строку:
	    -v /home/ros2/1/cont/src:/home/work \  и прописать вместо  /home/ros2/1/cont/src свой путь к скаченным файлам.
- `Dockerfile` – сборка образа `ros2_full:v1`
- `worlds/` – файлы миров Gazebo с цветными кубами 
- `config/` – конфигурация для RVIZ2
- `description/` – urdf-файл робота
- `launch/` – лаунч файл для запуска проекта
- `worlds/` – файлы миров Gazebo с цветными кубами 
- `src/` – нода для запуска робота, и его работы, в ноде описано, каким образом робот делает детекцию цвета куба




🔧 Если образ `ros2_full:v1` отсутствует (рекомендую перед запуском)

Собери его из `Dockerfile`:

bash
docker build -t ros2_full:v1 .

 📸 Пример работы



-

📝 Лицензия

MIT


