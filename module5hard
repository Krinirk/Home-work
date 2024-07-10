class User:
  def __init__(self, nickname: str, password: int, age: int):
    self.name = name
    self.password = password
    self.age = age


class Video:
  def __init__(self, title: str, duration: int, adult_mode: int):
    self.title = title
    self.duration = duration
    self.adult_mode = adult_mode
    time_now = 0


class UrTube:
  def __init__(self, users: list, videos: list, current_user: User):
    self.users = users
    self.videos = videos
    self.current_user = current_user

  
  def log_in(self, nickname: str, password):
    for user in self.users:
      if user.nickname == nickname and user.password == password:
        self.current_user = user
        return True
    return False

  
  def register(self, nickname: str, password: int, age: int):
    for user in self.users:
      if user.nickname == nickname:
        return False
    self.users.append(User(nickname, password, age))
    return True
  
  
  def log_out(self):
    self.current_user = None

  
  def add(self, *args):
    if len(args) == 3:
      self.videos.append(Video(args[0], args[1], args[2]))
    elif len(args) == 2:
      self.videos.append(Video(args[0], args[1], 0))
    else:
      self.videos.append(Video(args[0], 0, 0))
        

  def get_video(self, title: str):
    for video in self.videos:
      if lower(video.title) == lower(title):
        return video
    return None


  def watch_video(self, title: str):
    video = self.get_video(title)
    if video is None:
      return False
    
      
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
