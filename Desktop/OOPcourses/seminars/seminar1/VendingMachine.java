package seminars.seminar1;

import java.util.List;
import java.util.Set;

public interface VendingMachine {
    public void initProduct(Set<Product> productList);
    public Product getProduct(String name);
}
