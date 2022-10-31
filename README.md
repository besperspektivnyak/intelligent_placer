# Intelligent Placer

### Постановка задачи

Имеется фотография с нарисованным многоугольником и каким-то количеством объектов. Требуется определить поместятся ли все эти предметы одновременно в имеющуюся фигуру.
“Intelligent Placer” оформлен в виде python-библиотеки intelligent_placer_lib, которая поставляется каталогом intelligent_placer_lib с файлом intelligent_placer.py, содержащим функцию - точку входа:

```python
def check_image(<path_to_png_jpg_image_on_local_computer>[, <poligon_coordinates>])
```
которая возвращает список индексов вмещаемых предметов (предметы номеруются с 0 сверху вниз относительно фотографии).

```python
from intelligent_placer_lib import intelligent_placer
def test_intelligent_placer():
	assert intelligent_placer.check_image(“/path/to/my/image.png”)
```
Также требуется воспроизводимый intelligent_placer.ipynb, содержащий репрезентативные примеры работы алгоритма с оценками качества его работы и их визуализацией.

### Требования к входным данным

- Многоугольник выпуклый и имеет не более 7 вершин; нарисован темным маркером на белом листе бумаги и сфотографирован вместе с объектами; линии многоугольника имеют примерно одинаковую ширину.
- Все объекты заранее известны. Объекты полностью расположены на фотографии и их части не выходят за края; не перекрывают друг друга частично или полностью; располагаются ровно под листом с многоугольником и не выходят за его края; находятся на одной фотографии единожды, повторения не допускаются.
- Поверхность, на фоне которой делаются фотографии светлая и ровная, без рельефа.
- Фотографии должны быть сделаны при дневном освещении без дополнительных источников; сверху, перпендикулярно плоскости объекта на камеру не менее 10 мегапикселей. Расстояние до предметов не более 50 сантиметров. Объекты хорошо освещены и имеют четкие границы, фотография не смазанная и без засветов. Фотографии вертикально ориентированы, соотношение сторон 9:16. Фотографии цветные, не допускается цветовая коррекция: наложение фильтров, изменение яркости, контрастности, цветов и тд.

### Данные

Фотографии объектов, используемых в работе, доступны по [ссылке](https://drive.google.com/drive/folders/1oKmaeSegdZoENYuWhglnzF_I7gXS6ZCO?usp=sharing).

Датасет для алгоритма доступен по следующей [ссылке](https://drive.google.com/drive/folders/1of6Tl7QJ28B8qZvfPbPHsL-g9xVXK9GB?usp=sharing). Доступны две папки: 'no' и 'yes'. В первой папке расположены фотографии, при обработке которых алгоритм выдает ответ 'no', во второй папке - 'yes'.

Репрезентативные примеры с кратким описанием расположены в файле **examples.pdf**.

### Выходные данные

В конце работы программа должна дать ответ 'True' или 'False'. Ответ будет выводиться в консоль. Ответ 'True' дается, если все предметы на фотографии могут поместиться в нарисованном многоугольнике. В иных случая ответ будет 'False'.

### План работы алгоритма

1. Бинаризация изображения с помощью детектора Кэнни и морфологических операций
2. Нахождение и уточнение контуров предметов с помощью отличительных особенностей датасета
3. Упрощение контуров с помощью элементарных геометрических фигур
    * Возможны уточнения форм в зависимости от типа предмета (на данный момент просто прямоугольники)
4. Вычисление геометрических характеристик предметов
5. Сравнение с геометрическими характеристиками многоугольника
    * Реализована только обработка площади. 
    * TODO: высота и ширина, диагонали, самая длинная диагональ многоугольника
6. Даем ответ в зависимости от результатов пункта 5