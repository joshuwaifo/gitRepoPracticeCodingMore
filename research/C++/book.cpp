//
// Created by ojuwaifo on 23/08/2021.
//

// CHAPTER: preface

Mat bigImg;
resize(smallImg, bigImg, size, 0, 0, INTER_LINEAR);
dst.setTo(0);
bigImg.copyTo(dst, mask);

// CHAPTER: An Introduction to the Basics of OpenCV
cmake_minimum_required (VERSION 3.0)
project (CMakeTest)
add_executable( ${ PROJECT_NAME } main.cpp )

// # Create our hello world library
    add_library ( Hello hello.cpp hello.h )

// # Create our application that uses our new library