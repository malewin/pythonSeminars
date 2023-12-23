package homework.vendingHot;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import seminars.seminar1.BottleOfWater;
import seminars.seminar1.Product;
import seminars.seminar1.VendingMachine;


public class VendingHotDrinks implements VendingMachine{

    private Set<Product> hotDrinksList = new HashSet<>();
    
    @Override
    public void initProduct(Set<Product> hotDrinksList){
        this.hotDrinksList = hotDrinksList;
    }

    @Override
    public Product getProduct(String name){
        for (Product product : hotDrinksList) {
            if (product.getName().equals(name)) {
                return product;
            }
        }
        return null;
    }

    public Product getProduct(int temperature) {
        for (Product product : hotDrinksList) {
            if (((HotDrink) product).getTemperature() == temperature) {
                return product;
            }
        }
        return null;
    }

    public Product getID(int id) {
        for (Product product : hotDrinksList) {
            if (((HotDrink) product).getId() == id) {
                return product;
            }
        }
        return null;
    }

    public Product getProduct(String name, double volume){
         for (Product product : hotDrinksList) {
            if (product.getName().equals(name) && ((BottleOfWater) product).getVolume() == volume) {
                return product;
            }
        }
        return null;
    }
    public Product getProduct(String name, double volume, int temperature){
         for (Product product : hotDrinksList) {
            if (product.getName().equals(name) && (((BottleOfWater) product).getVolume() == volume) && (((HotDrink) product).getTemperature() == temperature)){
                return product;
            }
        }
        return null;
    }
}