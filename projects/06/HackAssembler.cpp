#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ifstream testfile;
    string goods;
    testfile.open("add/Add.asm");    //default ios mode is in because used ifstream constructor
    if(testfile.is_open()){
        while(testfile.get(goods,25)){
            cout << goods << '\n';
        }
        testfile.close();
    }
    else cout << "No work :(";

    cout << goods;

    return 0;
}