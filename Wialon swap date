import datetime
import time
import os


def main():
    with open(old_file, 'r', encoding='utf-8') as file:
        date1 = file.readlines()
        for a in date1:
            old_date = a.split(';')[1]
            dt = int(old_date)
            data = datetime.datetime.fromtimestamp(int(dt)).strftime(new_date + ' %H:%M:%S')
            unix_time = int(time.mktime(time.strptime(data, '%Y-%m-%d %H:%M:%S')))
            reg = a.split(';')[0]
            gps1 = a.split(';')[2]
            gps2 = a.split(';')[3]
            o1 = a.split(';')[4]
            o2 = a.split(';')[5]
            alt = a.split(';')[6]
            o4 = a.split(';')[7]
            o5 = a.split(';')[8]
            o6 = a.split(';')[9]
            try:
                path = 'result'
                if not os.path.exists(path):
                    os.mkdir(path)
            finally:
                with open('result\\' + old_file, 'a', encoding='cp1251') as f:
                    f.write(f'{reg};{unix_time};{gps1};{gps2};{o1};{o2};{alt};{o4};{o5};{o6};;\n')


if __name__ == '__main__':
    while True:
        old_file = input('Введите название старого файла: ')
        new_date = input('Введите день в формате yyyy-mm-dd: ')
        try:
            main()
            print('Выполнено!')
        except ValueError:
            print('')
        except FileNotFoundError:
            print(f'Файл {old_file} не найден!')
        except KeyboardInterrupt:
            print('Программа закрывается...')
            time.sleep(1)
            print('3...')
            time.sleep(1)
            print('2...')
            time.sleep(1)
            print('1...')
            exit()
