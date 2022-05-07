#include <iostream>
#include <fstream>
#include <string>
#include <typeinfo>

void get_goods(char *goods){
    std::ifstream assemblyCode;
    char c;
    assemblyCode.open("add/Add.asm");    //default ios mode is in because used ifstream constructor
    if(assemblyCode.is_open()){
        int i = 0;
        while(assemblyCode.get(c)){
            goods[i] = c;
            i++;
        }
        assemblyCode.close();
    }
    else std::cout << "No work :(" << std::endl;

    // std::cout << (goods) << std::endl;
    // std::cout << typeid(goods).name() << std::endl;
    // std::cout << "Printing, Printing, Printing" << std::endl;

}

int main(){
    
    int goods_size = 500;
    char goods[goods_size];
    get_goods(goods);
    std::cout << (goods) << std::endl;

    return 0;
}