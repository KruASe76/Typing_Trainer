# -*- coding: utf8 -*-
import pgzrun, time
from random import choice as ranch

WIDTH, HEIGHT = 830, 830
pause_time, dd_time, ddd_time, counter, lang, start, pause, win, choice, max_cps, list_cps, right, enter, appear, cheat=0, 0, 1, 0, 0, 0, 0, 10, 0, 0, [0.00], 0, '', 1, 0
word_list, coord_list=[], []
main_dict={(40, 265):'', (115, 265):'', (190, 265):'', (265, 265):'', (340, 265):'', (415, 265):'', (490, 265):'', (565, 265):'', (640, 265):'', (715, 265):'', (790, 265):'',
           (40, 340):'', (115, 340):'', (190, 340):'', (265, 340):'', (340, 340):'', (415, 340):'', (490, 340):'', (565, 340):'', (640, 340):'', (715, 340):'', (790, 340):'',
           (40, 415):'', (115, 415):'', (190, 415):'', (265, 415):'', (340, 415):'', (415, 415):'', (490, 415):'', (565, 415):'', (640, 415):'', (715, 415):'', (790, 415):'',
           (40, 490):'', (115, 490):'', (190, 490):'', (265, 490):'', (340, 490):'', (415, 490):'', (490, 490):'', (565, 490):'', (640, 490):'', (715, 490):'', (790, 490):'',
           (40, 565):'', (115, 565):'', (190, 565):'', (265, 565):'', (340, 565):'', (415, 565):'', (490, 565):'', (565, 565):'', (640, 565):'', (715, 565):'', (790, 565):'',
           (40, 640):'', (115, 640):'', (190, 640):'', (265, 640):'', (340, 640):'', (415, 640):'', (490, 640):'', (565, 640):'', (640, 640):'', (715, 640):'', (790, 640):'',
           (40, 715):'', (115, 715):'', (190, 715):'', (265, 715):'', (340, 715):'', (415, 715):'', (490, 715):'', (565, 715):'', (640, 715):'', (715, 715):'', (790, 715):'',
           (40, 790):'', (115, 790):'', (190, 790):'', (265, 790):'', (340, 790):'', (415, 790):'', (490, 790):'', (565, 790):'', (640, 790):'', (715, 790):'', (790, 790):''}
for i in main_dict.keys():
    coord_list.append(i)

def cheat_fun():
    global cheat
    cheat=1
    clock.schedule(uncheat, 2.5)

def uncheat():
    global cheat
    cheat=0

def wait():
    time.sleep(0.8)

def end():
    global start
    start=5
def clean():
    global right
    right=0

def clean1():
    global enter
    enter=''

def appear_fun():
    global main_dict, start, lang, word_list, coord_list, appear
    if lang==1:
        let_list=list('ЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬ')
    elif lang==2:
        let_list=list('QWERTYUIOPASDFGHJKLZXCVBNM')
    let1=ranch(let_list)
    let_list.remove(let1)
    let2=ranch(let_list)
    word=let1+let2
    while word in word_list:
        if lang==1:
            let_list=ru_letters
        elif lang==2:
            let_list=en_letters
        let1=ranch(let_list)
        let_list.remove(let1)
        let2=ranch(let_list)
        word=let1+let2
    word_list.append(word.lower())
    try:
        crd=ranch(coord_list)
        coord_list.remove(crd)
        main_dict[crd]=word
    except IndexError:
        pass
    
    appear=1

def on_mouse_down(pos):
    global start, lang, choice, d_time, pause, now_time, counter, pause_time, main_dict, word_list, dd_time, ddd_time, win, choice, max_cps, list_cps, right, enter, appear, cheat
    if start==0:
        if Rect(365, 620, 103, 50).collidepoint(pos):
            start=1
    elif start==1:
        if Rect(145, 350, 200, 200).collidepoint(pos):
            start=2
            lang=1
        elif Rect(475, 350, 200, 200).collidepoint(pos):
            start=2
            lang=2
    elif start==2:
        if Rect(0, 310, 830, 50).collidepoint(pos):
            choice=1
        elif Rect(0, 360, 830, 50).collidepoint(pos):
            choice=2
        elif Rect(0, 410, 830, 50).collidepoint(pos):
            choice=3
        elif Rect(310, 544, 210, 50).collidepoint(pos):
            if choice==1:
                d_time=2.2
                start=3
            elif choice==2:
                d_time=1.95
                start=3
            elif choice==3:
                d_time=1.7
                start=3
    elif start==3:
        if Rect(265, 300, 300, 300).collidepoint(pos):
            start=14
    elif start==4:
        if pause==0:
            if Rect(755, 5, 70, 70).collidepoint(pos):
                pause=1
        elif pause==1:
            if Rect(755, 5, 70, 70).collidepoint(pos):
                pause=0
            elif Rect(315, 500, 200, 200).collidepoint(pos):
                start=5
    elif start==5:
        if Rect(180, 500, 200, 200).collidepoint(pos):
            pause_time, dd_time, ddd_time, counter, lang, start, pause, win, choice, max_cps, list_cps, right, enter, appear, cheat, word_list=0, 0, 1, 0, 0, 0, 0, 10, 0, 0, [0.00], 0, '', 1, 0, []
            for i in main_dict.keys():
                main_dict[i]=''
                coord_list.append(i)
        elif Rect(450, 500, 200, 200).collidepoint(pos):
            exit()

def on_key_down(key,mod,unicode):
    global enter, main_dict, right, word_list, pause, dd_time, ddd_time, coord_list, counter
    if lang==1:
        let_list=list('ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'.lower())
    elif lang==2:
        let_list=list('QWERTYUIOPASDFGHJKLZXCVBNM'.lower())
    for i in range(len(let_list)):
        let_list[i]=let_list[i].lower()
    if start==4:
        if pause==0:
            if unicode in let_list:
                enter1=enter+unicode.upper()
                enter=enter1
            if len(enter)==2:
                for i in main_dict.keys():
                    if enter==main_dict[i]:
                        right=1
                        clock.schedule(clean, 0.5)
                        clock.schedule(clean1, 0.2)
                        word_list.remove(main_dict[i].lower())
                        coord_list.append(i)
                        main_dict[i]=''
                        counter+=1
                        ddd_time=ddd_time/2
                        dd_time+=ddd_time
                        break
                else:
                    right=2
                    clock.schedule(clean, 0.5)
                    clock.schedule(clean1, 0.2)
            if len(enter)>2:
                enter=enter[0]+enter[1]
            if key==keys.BACKSPACE or key==keys.DELETE:
                enter=''
        elif pause==1:
            if unicode in let_list:
                clock.schedule(cheat_fun, 0.01)

def update():
    global start, main_dict, cps, list_cps, max_cps, now_time, start_time, counter, pause, d_time, dd_time, appear, pause_time, win
    if start==14:
        start=13
    elif start==13:
        time.sleep(1.0)
        start=12
    elif start==12:
        time.sleep(1.0)
        start=11
    elif start==11:
        time.sleep(1.0)
        start=10
    elif start==10:
        time.sleep(1.0)
        start_time=time.time()
        now_time=time.time()-start_time
        if now_time>0:
            cps=(counter/now_time)//0.001/1000
        else:
            cps=0.000
        if cps!=list_cps[-1]:
            list_cps.append(cps)
        start=4
    
    elif start==4:
        if pause==0:
            now_time=(time.time()-start_time-pause_time)
            if now_time>0:
                cps=(counter/now_time)//0.001/1000
            else:
                cps=0.000
            if cps!=list_cps[-1]:
                list_cps.append(cps)
        
            if appear==1:
                zxcv=d_time-dd_time
                clock.schedule(appear_fun, zxcv)
                appear=0
            if cps!=list_cps[-1]:
                list_cps.append(cps)
        elif pause==1:
            pause_time=time.time()-start_time-now_time
        
        for i in main_dict.values():
            if i=='':
                break
        else:
            clock.schedule(wait, 0.01)
            win=0
            clock.schedule(end, 0.02)
            
        if now_time>=180:
            now_time=180
            clock.schedule(wait, 0.01)
            win=1
            clock.schedule(end, 0.02)
        

def draw():
    global main_dict, choice, start, counter, now_time, cps, list_cps, word_list, enter, right, pause, cheat
    screen.fill((250, 223, 173))
    if start==0:
        screen.draw.text('                       Здравствуйте!\n\n\n                Это клавиатурный тренажер.\n\n   Через некоторый промежуток времени один из кругов на\n поле становится черным, и внутри него появляются 2 буквы.\n\n       Введите указанные буквы с клавиатуры, чтобы\n             заполненный круг сделать пустым.\n\n   Вы проиграете, если все круги на поле будут заполнены.\n\n       Чтобы пройти уровень, достаточно продержаться\n                        3 мин 20 cек\n\n\n                           Удачи!', (3, 35), fontname='jbm-r', fontsize=24, color=(0, 0, 0))
        screen.draw.filled_rect(Rect(370, 620, 103, 50), (255, 165, 0))
        screen.draw.rect(Rect(370, 620, 103, 50), (0, 0, 0))
        screen.draw.text('Далее', (376.5, 624), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
    elif start==1:
        screen.draw.text('Выберите раскладку', (205, 170), fontname='jbm-r', fontsize=40, color=(0, 0, 0))
        screen.blit('ru_flag', (145, 350))
        screen.blit('en_flag', (475, 350))
        screen.draw.text('Русская', (185, 570), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
        screen.draw.text('Английская', (484.5, 570), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
    elif start==2:
        screen.draw.text('Выберите уровень сложности', (142, 145), fontname='jbm-r', fontsize=37, color=(0, 0, 0))
        screen.draw.text('Легкий', (41.5, 320), fontname='jbm-r', fontsize=25, color=(0, 0, 0))
        screen.draw.text('Средний', (40, 370), fontname='jbm-r', fontsize=25, color=(0, 0, 0))
        screen.draw.text('Сложный', (40, 420), fontname='jbm-r', fontsize=25, color=(0, 0, 0))
        screen.draw.line((39, 360), (791, 360), (0, 0, 0))
        screen.draw.line((39, 411), (791, 411), (0, 0, 0))
        screen.draw.rect(Rect(760, 320, 30, 30), (0, 0, 0))
        screen.draw.rect(Rect(760, 370, 30, 30), (0, 0, 0))
        screen.draw.rect(Rect(760, 420, 30, 30), (0, 0, 0))
        if choice==1:
            screen.blit('tick', (762, 321.5))
        elif choice==2:
            screen.blit('tick', (762, 371.5))
        elif choice==3:
            screen.blit('tick', (762, 421.5))
        screen.draw.filled_rect(Rect(310, 544, 210, 50), (255, 165, 0))
        screen.draw.rect(Rect(310, 544, 210, 50), (0, 0, 0))
        screen.draw.text('Подтвердить', (317, 550), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
    elif start==3:
        screen.draw.text('Вы готовы начать игру?', (160, 150), fontname='jbm-r', fontsize=40, color=(0, 0, 0))
        screen.blit('play_button', (265, 300))
    elif start==4:
        now_time1=str(int(now_time//60))
        if now_time%60<10:
            now_time2='0'+str(int(now_time)%60)
        else:
            now_time2=str(int(now_time)%60)
        now_time3=str(int(now_time//0.001%1000))
        if pause==0:
            for i in main_dict.keys():
                if main_dict[i]=='':
                    screen.draw.circle(i, 35, (0, 0, 0))
                else:
                    screen.draw.filled_circle(i, 35, (0, 0, 0))
                    i1=(i[0]-18,i[1]-18)
                    screen.draw.text(main_dict[i], i1, fontname='jbm-r', fontsize=30, color=(250, 223, 173))
            screen.draw.line((350, 0), (350, 225), (0, 0, 0))
            screen.draw.line((0, 225), (830, 225), (0, 0, 0))
            screen.blit('pause_button', (755, 5))
            
            screen.draw.text('   С', (8, 17.6), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
            screen.draw.text('    татистика:', (8, 18), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
            screen.draw.text(f'\n\n        Время: {now_time1}:{now_time2}:{now_time3}', (10, 20), fontname='jbm-r', fontsize=23, color=(0, 0, 0))
            screen.draw.text(f'\n\n\n        Вводы: {counter}', (10, 20), fontname='jbm-r', fontsize=23, color=(0, 0, 0))
            screen.draw.text(f'\n\n\n\n    Вводы/сек: {cps}', (10, 20), fontname='jbm-r', fontsize=23, color=(0, 0, 0))
            screen.draw.text(f'\n\n\n\n\nЗаполн.кругов: {len(word_list)}/88', (10, 20), fontname='jbm-r', fontsize=23, color=(0, 0, 0))
            screen.draw.text(f'Строка ввода: {enter}', (380, 17.6), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
            screen.draw.line((620, 50), (678, 50), (0, 0, 0))
            if right==1:
                screen.blit('right', (480, 63))
            elif right==2:
                screen.blit('wrong', (480, 63))
        elif pause==1:
            screen.draw.line((350, 0), (350, 225), (0, 0, 0))
            screen.draw.line((0, 225), (830, 225), (0, 0, 0))
            screen.blit('play_button1', (755, 5))
        
            screen.draw.text('   С', (8, 17.6), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
            screen.draw.text('    татистика:', (8, 18), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
            screen.draw.text(f'\n\n        Время: {now_time1}:{now_time2}:{now_time3}', (10, 20), fontname='jbm-r', fontsize=23, color=(0, 0, 0))
            screen.draw.text(f'\n\n\n        Вводы: {counter}', (10, 20), fontname='jbm-r', fontsize=23, color=(0, 0, 0))
            screen.draw.text(f'\n\n\n\n    Вводы/сек: {cps}', (10, 20), fontname='jbm-r', fontsize=23, color=(0, 0, 0))
            screen.draw.text(f'\n\n\n\n\nЗаполн.кругов: {len(word_list)}/88', (10, 20), fontname='jbm-r', fontsize=23, color=(0, 0, 0))
            screen.draw.text(f'Строка ввода: {enter}', (380, 17.6), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
            screen.draw.line((620, 50), (678, 50), (0, 0, 0))
            
            screen.draw.text('Игра приостановлена', (250, 300), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
            screen.blit('power_icon1', (320, 500))
            
            if cheat==1:
                screen.draw.text('             А тех, кто будет жульничать...', (32, 400), fontname='jbm-r', fontsize=24, color=(0, 0, 0))
    elif start==5:
        now_time1=str(int(now_time//60))
        if now_time%60<10:
            now_time2='0'+str(int(now_time)%60)
        else:
            now_time2=str(int(now_time)%60)
        now_time3=str(int(now_time//0.001%1000))
        if win==10:
            screen.draw.text('Игра прервана', (250, 120), fontname='jbm-r', fontsize=40, color=(0, 0, 0))
        elif win==1:
            screen.draw.text('Вы справились! :)', (215, 120), fontname='jbm-r', fontsize=40, color=(0, 0, 0))
        elif win==0:
            screen.draw.text('К сожалению,', (265, 70), fontname='jbm-r', fontsize=40, color=(0, 0, 0))
            screen.draw.text('Вы не справились :(', (181, 120), fontname='jbm-r', fontsize=40, color=(0, 0, 0))
        if d_time==2.2:
            screen.draw.text(f'        Уровень: Легкий', (200, 200), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
        elif d_time==1.95:
            screen.draw.text(f'        Уровень: Средний', (200, 200), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
        elif d_time==1.7:
            screen.draw.text(f'        Уровень: Сложный', (200, 200), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
        screen.draw.text(f'          Вводы: {counter}', (200, 240), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
        screen.draw.text(f'          Время: {now_time1}:{now_time2}:{now_time3}', (200, 280), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
        screen.draw.text(f'Сред. вводы/сек: {(sum(list_cps)/len(list_cps))//0.001/1000}', (200, 320), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
        screen.draw.text(f'Макс. вводы/сек: {max(list_cps)}', (200, 360), fontname='jbm-r', fontsize=30, color=(0, 0, 0))
        
        screen.blit('restart_icon', (180, 500))
        screen.blit('exit_icon', (450, 500))
    elif start==13:
        screen.draw.text('3', (270, 130), fontname='jbm-r', fontsize=500, color=(0, 0, 0))
    elif start==12:
        screen.draw.text('2', (270, 130), fontname='jbm-r', fontsize=500, color=(0, 0, 0))
    elif start==11:
        screen.draw.text('1', (270, 130), fontname='jbm-r', fontsize=500, color=(0, 0, 0))
    elif start==10:
        screen.draw.text('GO!', (90, 160), fontname='jbm-r', fontsize=400, color=(0, 0, 0))
    
    
    
pgzrun.go()