package seminars.seminar1;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class BottleOfWaterVendingMachine implements VendingMachine{

    private Set<Product> productList = new HashSet<>();

    @Override
    public void initProduct(Set<Product> productList){
        this.productList = productList;
    }

    @Override
    public Product getProduct(String name){
        for (Product product : productList) {
            if (product.getName().equals(name)) {
                return product;
            }
        }
        return null;
    }

    public Product getProduct(String name, double volume){
         for (Product product : productList) {
            if (product.getName().equals(name) && ((BottleOfWater) product).getVolume() == volume) {
                return product;
            }
        }
        return null;
    }
}
