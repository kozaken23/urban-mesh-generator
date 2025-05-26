
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <map>
#include <algorithm>
#include<numeric>

// ファイルからデータを読み込む関数
void read_data(const std::string& input_filename, std::vector<double>& x, std::vector<double>& y, std::vector<double>& z) {
    std::ifstream input_data(input_filename);
    if(!input_data.is_open()) {
        std::cerr<<"Error : "<<input_filename<<std::endl;
        exit(1);
    }
    double temp_x, temp_y, temp_z;
    while(input_data >> temp_x >> temp_y >> temp_z) {
        x.push_back(temp_x);
        y.push_back(temp_y);
        z.push_back(std::max(temp_z, 0.0));  // zの値が負の場合は0にする
    }
    input_data.close();
}

// xとyの最小値と最大値を計算する関数
std::pair<double, double> find_min_max(const std::vector<double>& data){
    double min_val=*std::min_element(data.begin(), data.end());
    double max_val=*std::max_element(data.begin(), data.end());
    return {min_val, max_val};
}

// グリッド化してデータを削減する関数
void grid_data(const std::map<std::pair<double, double>, double>& p, std::map<std::pair<double, double>, double>& sakugen, int grid_size, double x_min, double x_max, double y_min, double y_max) {
    int num=0;
    int l=0;
    for(int i=static_cast<int>(x_min); i<=static_cast<int>(x_max); i+=grid_size){
        for(int j=static_cast<int>(y_min); j<=static_cast<int>(y_max); j+=grid_size){
            num++;
            std::vector<double> grid_values;
            for(int m=0; m<grid_size; m++){
                for(int n=0; n<grid_size; n++){
                    auto it=p.find({i+m, j+n});
                    if(it!=p.end()){
                        grid_values.push_back(it->second);
                    }else{
                        grid_values.push_back(0);
                    }
                }
            }
            if(std::all_of(grid_values.begin(), grid_values.end(), [](double v) { return v != 0; })){
                double grid_mean=std::accumulate(grid_values.begin(), grid_values.end(), 0.0)/grid_values.size();
                double center_x=i+grid_size/2.0;
                double center_y=j+grid_size/2.0;
                sakugen[{center_x, center_y}]=grid_mean;
            } else {
                l++;
                double center_x=i+grid_size/2.0;
                double center_y=j+grid_size/2.0;
                sakugen[{center_x, center_y}]=0;
            }
        }
    }
    std::cout<<l<<std::endl;
    std::cout<<"グリッドの数 "<<num<<" grid cells"<<std::endl;
    std::cout<<"削減後の行数 : "<<sakugen.size()<<std::endl;
}

int main() {
    std::string input_filename="jimen.dat";
    std::vector<double>x,y,z;

    // データを読み込む
    read_data(input_filename, x, y, z);

    // xとyの最小値と最大値を計算する
    auto x_minmax=find_min_max(x);
    auto y_minmax=find_min_max(y);
    double x_min=x_minmax.first, x_max=x_minmax.second;
    double y_min=y_minmax.first, y_max=y_minmax.second;

    // 辞書pの初期化
    std::map<std::pair<double, double>, double> p;
    for (size_t i=0; i<z.size(); i++) {
        p[{x[i], y[i]}]=z[i];
    }

    // グリッドサイズの設定とデータ削減
    int grid_size=3;
    std::map<std::pair<double, double>, double> sakugen;
    grid_data(p, sakugen, grid_size, x_min, x_max, y_min, y_max);

    std::cout<<"削減率: "<<100.0-100.0*sakugen.size()/p.size()<<"%"<<std::endl;

    // 結果をファイルに書き込む
    std::string output_filename="sjimen.dat";
    std::ofstream output_file(output_filename);
    if (!output_file.is_open()) {
        std::cerr << "Error opening file: " << output_filename << std::endl;
        exit(1);
    }
    for (int i=static_cast<int>(x_min); i<=static_cast<int>(x_max); i+=grid_size) {
        for (int j=static_cast<int>(y_min); j<=static_cast<int>(y_max); j+=grid_size) {
            output_file << std::fixed << std::setprecision(2) 
                        << static_cast<float>(i+grid_size/2.0) << " " 
                        << static_cast<float>(j+grid_size/2.0) << " " 
                        << sakugen[{i+grid_size/2.0, j+grid_size/2.0}] << std::endl;
        }
    }
    output_file.close();

    //tatemono
    std::string input_filename2="tatemono.dat";
    std::vector<double>x2,y2,z2;

    // データを読み込む
    read_data(input_filename2, x2, y2, z2);

    // xとyの最小値と最大値を計算する
    auto x_minmax2=find_min_max(x2);
    auto y_minmax2=find_min_max(y2);
    double x_min2=x_minmax2.first, x_max2=x_minmax2.second;
    double y_min2=y_minmax2.first, y_max2=y_minmax2.second;

    // 辞書pの初期化
    std::map<std::pair<double, double>, double> p2;
    for (size_t i=0; i<z2.size(); i++) {
        p2[{x2[i], y2[i]}]=z2[i];
    }

    // データ削減
    int grid_size2=2;
    std::map<std::pair<double, double>, double> sakugen2;
    grid_data(p2, sakugen2, grid_size2, x_min2, x_max2, y_min2, y_max2);

    std::cout<<"削減率: "<<100.0-100.0*sakugen2.size()/p2.size()<<"%"<<std::endl;

    // 結果をファイルに書き込む
    std::string output_filename2="statemono.dat";
    std::ofstream output_file2(output_filename2);
    if (!output_file2.is_open()) {
        std::cerr << "Error opening file: " << output_filename2 << std::endl;
        exit(1);
    }
    for (int i=static_cast<int>(x_min2); i<=static_cast<int>(x_max2); i+=grid_size2) {
        for (int j=static_cast<int>(y_min2); j<=static_cast<int>(y_max2); j+=grid_size2) {
            output_file2 << std::fixed << std::setprecision(2) 
                        << static_cast<float>(i+grid_size2/2.0) << " " 
                        << static_cast<float>(j+grid_size2/2.0) << " " 
                        << sakugen2[{i+grid_size2/2.0, j+grid_size2/2.0}] << std::endl;
        }
    }
    output_file2.close();

    return 0;
}
