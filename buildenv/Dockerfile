ARG IMAGE=alpine:3.22.1

FROM $IMAGE

RUN  apk add zsh git curl wget g++ clang boost-static ninja boost-dev cmake make sudo bash vim libressl-dev util-linux-dev zlib-dev zlib-static patch zstd-static util-linux-static

RUN mkdir /buildenv

WORKDIR /buildenv

RUN curl -JO 'https://developer.apple.com/file/?file=security&agree=Yes' -H 'Referer: https://developer.apple.com/security/' && unzip corecrypto.zip
WORKDIR /buildenv/corecrypto-2024
RUN sed '/coverage/d' -i "CMakeLists.txt"
RUN mkdir corecrypto_static && mv ccrng_static.c corecrypto_static/ccrng_static.c
RUN mkdir build; cd build; CC=clang CXX=clang++ cmake ..;
WORKDIR /buildenv/corecrypto-2024/build
RUN sed -i -E 's|^(all: CMakeFiles\/corecrypto_perf)|#\1|' CMakeFiles/Makefile2; sed -i -E 's|^(all: CMakeFiles\/corecrypto_test)|#\1|' CMakeFiles/Makefile2
RUN make -j6; make install

WORKDIR /buildenv

RUN git clone --recursive https://github.com/microsoft/cpprestsdk; 
WORKDIR /buildenv/cpprestsdk
RUN sed -i 's|-Wcast-align||' "./Release/CMakeLists.txt"
RUN mkdir build; cd build; cmake -DBUILD_SHARED_LIBS=0 -DWERROR=OFF ..; make -j6; make install

WORKDIR /buildenv/

RUN git clone https://github.com/nih-at/libzip && cd libzip; mkdir build; cd build; cmake -DBUILD_SHARED_LIBS=0 ..; make -j6; make install


