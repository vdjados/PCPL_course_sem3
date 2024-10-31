import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    private static boolean isEqual(double x, double y) {
        return Math.abs(x - y) < 1e-10; // Используем небольшую epsilon для сравнения
    }

    private static List<Double> getRoots(double a, double b, double c) {
        List<Double> result = new ArrayList<>();
        int d = (int) (b * b - 4 * a * c);

        if (isEqual(d, 0)) {
            result.add(-b / (2 * a));
        } else if (d > 0) {
            double sqD = Math.sqrt(d);
            result.add((-b + sqD) / (2.0 * a));
            result.add((-b - sqD) / (2.0 * a));
        }

        List<Double> finalResult = new ArrayList<>();
        for (double root : result) {
            if (isEqual(root, 0.0)) {
                finalResult.add(0.0);
            } else if (root > 0) {
                finalResult.add(Math.sqrt(root));
                finalResult.add(-Math.sqrt(root));
            }
        }

        return finalResult;
    }

    public static void main(String[] args) {
        double a, b, c;

        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите коэффициент A: ");
        a = scanner.nextDouble();
        System.out.print("Введите коэффициент B: ");
        b = scanner.nextDouble();
        System.out.print("Введите коэффициент C: ");
        c = scanner.nextDouble();

        // Проверка на 0 для коэффициента a
        if (isEqual(a, 0)) {
            System.out.println("Коэффициент A не может быть равен 0.");
            return;
        }

        List<Double> roots = getRoots(a, b, c);
        int lenRoots = roots.size();

        switch (lenRoots) {
            case 0:
                System.out.println("Нет корней.");
                break;
            case 1:
                System.out.println("Один корень: " + roots.get(0));
                break;
            case 2:
                System.out.println("Два корня: " + roots.get(0) + " и " + roots.get(1));
                break;
            case 3:
                System.out.println("Три корня: " + roots.get(0) + ", " + roots.get(1) + " и " + roots.get(2));
                break;
            case 4:
                System.out.println("Четыре корня: " + roots.get(0) + ", " + roots.get(1) + ", " + roots.get(2) + ", " + roots.get(3));
                break;
            default:
                break;
        }

        scanner.close();
    }
}
