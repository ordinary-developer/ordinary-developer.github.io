Title: Creating a simple Qt app with resources
Date: 2018-12-21 21:43
Modified: 2018-12-21 21:43
Category: Qt
Tags: Qt, C++
Authors: Tutov Yevgeni
Summary: Creating a simple Qt application with resources from scratch


This post describes creation of a simple qt application with resources from scratch.
The code here is not very dificult,
but this post mainly shows neccessary console commands for building an application.

Let's suppose we have a main file:
```
#include <QtWidgets>

int main(int argc, char** argv) {
    QApplication app{argc, argv};
    QWidget widget{};

    QWidget* childWidget1{ new QWidget{&widget} };
    QPalette palette1{};
    palette1.setColor(childWidget1->backgroundRole(), Qt::blue);
    childWidget1->setPalette(palette1);
    childWidget1->resize(100, 100);
    childWidget1->move(25, 25);
    childWidget1->setAutoFillBackground(true);

    QWidget* childWidget2{new QWidget{&widget}};
    QPalette palette2{};
    palette2.setBrush(childWidget2->backgroundRole(), 
                      QBrush{QPixmap{":/image.jpg"}});
    childWidget2->setPalette(palette2);
    childWidget2->resize(100, 100);
    childWidget2->move(75, 75);
    childWidget2->setAutoFillBackground(true);

    widget.resize(200, 200);
    widget.show();

    return app.exec();
}
```

First we must create a resoure file (let it be an images.qrc)
```
<!DOCTYPE RCC><RCC version="1.0">
<qresource>
    <file alias="image.jpg">images/image.jpg</file>
</qresource>
</RCC>
```

To compile it and get a binary file we must perform the next steps:

- Enter the project directory:
```sh
$ cd project_dir
```

- Run:
```sh
$ qmake -project
```

- After that a pro-file with the name equal to the parent directory name will be generated, add the next strings to this file:
```   
QT += widgets
QMAKE_CXXFLAGS += -std=c++17 -Wall -Wextra -pedantic
RESOURCES = images.qrc
```
(if you want to compile your code with other parameters specify your own parameters)


- After that run the next command to create a makefile:
```sh
$ qmake
```

- After that run the next command:
```sh
$ make
```
for parallel compiling run:
```sh
$ make --jobs 4
```


