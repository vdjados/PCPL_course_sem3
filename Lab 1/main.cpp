#include <iostream>
#include <vector>
#include <limits>
#include <cmath>
using namespace std;

bool is_equal(double x, double y) {
    return std::fabs(x - y) < std::numeric_limits<double>::epsilon();
}

vector<double> get_roots(double a, double b, double c) {
    vector<double> result;
    int d = b * b - 4 * a * c;

    if (is_equal(d, 0)) {
        result.push_back(-b / (2 * a));
    } else if (d > 0) {
        double sqD = sqrt(d);
        result.push_back((-b + sqD) / (2.0 * a));
        result.push_back((-b - sqD) / (2.0 * a));
    }

    vector<double> final_result;
    for (double root : result) {
        if (is_equal(root, 0.0)) {
            final_result.push_back(0);
        } else if (root > 0) {
            final_result.push_back(sqrt(root));
            final_result.push_back(-sqrt(root));
        }
    }

    return final_result;
}

int main(int argc, char* argv[]) {
    double a, b, c;
    if (argc == 4) {
        a = atof(argv[1]);
        b = atof(argv[2]);
        c = atof(argv[3]);
    } else {
        cout << "Введите коэффициент A: ";
        cin >> a;
        cout << "Введите коэффициент B: ";
        cin >> b;
        cout << "Введите коэффициент C: ";
        cin >> c;
    }

    // Проверка на 0 для коэффициента a
    if (is_equal(a, 0)) {
        cout << "Коэффициент A не может быть равен 0." << endl;
        return -1;
    }

    vector<double> roots = get_roots(a, b, c);
    int len_roots = roots.size();
    switch (len_roots) {
        case 0:
            cout << "Нет корней." << endl;
            break;
        case 1:
            cout << "Один корень: " << roots[0] << endl;
            break;
        case 2:
            cout << "Два корня: " << roots[0] << " и " << roots[1] << endl;
            break;
        case 3:
            cout << "Три корня: " << roots[0] << ", " << roots[1] << " и " << roots[2] << endl;
            break;
        case 4:
            cout << "Четыре корня: " << roots[0] << ", " << roots[1] << ", " << roots[2] << ", " << roots[3] << endl;
            break;
        default:
            break;
    }

    return 0;
}
