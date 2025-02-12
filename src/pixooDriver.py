import time
from pixoo import Channel, ImageResampleMode, Pixoo
import util
class PixooDriver:
  def __init__(self, ip):
    self.pixoo = Pixoo(ip)

    if self.pixoo is None:
      print('Failed to connect to Pixoo')
      exit(1)
    else:
      print('Connected to Pixoo') 
    
    # get the current clock and channel
    self.clock_channel()

    # set the colors
    self.colors= {  
      'background': (20, 33, 61),
      'status': (252, 163, 17),
      'title': (245, 203, 92),
      'text': (255, 255, 255),
      'line': (229, 229, 229)
    }
  
  # get the current clock and channel
  def clock_channel(self):
    config = self.pixoo.get_all_device_configurations()
    self.clock = config['CurClockId']
    self.channel = self.get_channel()
  
  # tokenize the text to fit the screen
  # return a dictionary with the position of each word
  def token_text(self, text):
    text_dict = {}
    texts = text.split(' ')
    i = 0

    for t in texts:
      text_dict.update({i: t})
      i += len(t) +1
    return text_dict

  # draw text on the screen
  def draw_text(self, text, xy, color):
    texts_token = self.token_text(text)

    print(texts_token) #debug
    row = 0
    x = xy[0]

    # draw the text
    for key in texts_token:
      offset = key * 4

      # if the text is too long, go to the next row
      if(key + len(texts_token[key]) > 15):
        row += 1
        x = xy[0]
        offset = 0
        
      self.pixoo.draw_text(texts_token[key], (x + offset, xy[1] + row * 10), color)

    self.push()

  # push the image to the screen
  def push(self):
    self.pixoo.push()

  # draw a line on the screen
  def draw_line(self, xy1, xy2, color):
    self.pixoo.draw_line(xy1, xy2, color)

  # draw a task on the screen
  def draw_task(self,task):
    self.pixoo.draw_line((2, 9), (62, 9), self.colors['line'])
    self.pixoo.draw_text(task["title"], (2, 12), self.colors['title'])
    self.draw_text(task["description"], (2, 22), self.colors['text'])
    self.push()

  # draw a rectangle on the screen from top left to bottom right
  def draw_rect(self, xy1, xy2, color):
    self.pixoo.draw_filled_rectangle(xy1, xy2, color)

  # draw all tasks on the screen
  def draw_all_tasks(self,tasks,status):
    self.pixoo.clear()
    
    # if there are no tasks
    if(len(tasks) == 0):
      #background
      self.draw_rect((0, 0), (64, 64), self.colors['background'])
      #Status
      self.pixoo.draw_text(status, (2, 2), self.colors['status'])
      self.draw_text("No tasks", (2, 12), self.colors['title'])
      self.pixoo.draw_line((2, 9), (62, 9), self.colors['line'])

      self.push()
      time.sleep(5)
      return
    
    # draw each task
    for task in tasks:
      self.pixoo.clear()
      #background
      self.draw_rect((0, 0), (64, 64), self.colors['background'])
      #Status
      self.pixoo.draw_text(status, (2, 2), self.colors['status'])
      self.draw_task(task);
      time.sleep(5)

  # reset the channel
  def reset_channel(self):
    print('Resetting channel to', self.channel)
    self.pixoo.set_channel(self.channel)
  
  # reset the clock
  def reset_clock(self):
    print('Resetting clock to', self.clock)
    self.pixoo.set_clock(self.clock)

  # revert the display
  def revert_display(self):
    self.pixoo.clear()
    self.reset_channel()
    #self.reset_clock()
  
  # get the current channel
  def get_channel(self):
    data = util.request(f"http://{util.enum['PIXOO_IP']}:80/post", {"Command": "Channel/GetIndex"})
    print(data)
    return data['SelectIndex']