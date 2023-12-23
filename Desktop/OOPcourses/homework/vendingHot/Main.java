package homework.vendingHot;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import seminars.seminar1.Product;

public class Main {
    public static void main(String[] args) {
        HotDrink hotDrink = new HotDrink("tea", 80, 0.250, 60, 1);
        HotDrink hotDrink1 = new HotDrink("capuccino", 160, 0.250, 80, 2);
        HotDrink hotDrink2 = new HotDrink("latte", 210, 0.250, 70, 3);
        HotDrink hotDrink3 = new HotDrink("tea with lemon", 110, 0.250, 55, 4);
        Set<Product> hotDrinks = new HashSet<>();
        hotDrinks.add(hotDrink);
        hotDrinks.add(hotDrink1);
        hotDrinks.add(hotDrink2);
        hotDrinks.add(hotDrink3);
        System.out.println("\u001B[34m"+"MENU:" + "\u001B[0m");
        System.out.println("\u001B[32m"+(hotDrinks.toString().replace(',', '\n'))+ "\u001B[0m");
        VendingHotDrinks vendingHot = new VendingHotDrinks();
        vendingHot.initProduct(hotDrinks);
        // System.out.println("Your choice:");
        // System.out.println(vendingHot.getProduct("tea", 0.250, 60));
        // System.out.println(vendingHot.getProduct(70));



        Map<String, Object> fltrBuffer = new HashMap<>();
        Scanner scanner = new Scanner(System.in);
        boolean search = true;

        while (search) {
            System.out.println("\u001B[34m"+"Покупка товара по ID: " + "\u001B[0m");
            System.out.println("1 - ID\n2 - Купить");
            int choice = scanner.nextInt();

            switch (choice){
                case 1:
                    System.out.println("Введите ID товара: ");
                    int idFilter = scanner.nextInt();
                    fltrBuffer.put("id", idFilter);
                    System.out.println("\u001B[33m" + "Выбранный id: " + fltrBuffer+ "\u001B[0m");
                    break;           
                case 2:
                    printFiltered((Set<Product>) hotDrinks, fltrBuffer);
                    search = false;
                    break;

                default:
                    System.out.println("Такого пункта нет в меню");
                    return;
            }

        }
    }

    static void printFiltered(Set<Product> hotDrinks, Map<String, Object> filterBuf){
        for (Product hotDrink: hotDrinks) {
            boolean matchesFilter = ((HotDrink) hotDrink).contains(filterBuf);

            if (matchesFilter) System.out.println("\u001B[32m"+"Ваш выбор: " + hotDrink+ "\u001B[0m");
        }
    }


}

