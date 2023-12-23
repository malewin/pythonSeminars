package homework.vendingHot;

import java.util.Map;

import seminars.seminar1.BottleOfWater;

public class HotDrink extends BottleOfWater{
    private int temperature;
    private int id;

    public HotDrink(String name, int cost, double volume, int temperature, int id){
        super(name,cost,volume);
        this.temperature = temperature;
        this.id = id;
    }

    public int getId(){
        return id;
    }

    public void setId(int id){
        this.id = id;
    }

    public int getTemperature(){
        return temperature;
    }

    public void setTemperature(int temperature){
        this.temperature = temperature;
    }

    @Override
    public String toString(){
        return "HotDrink{" +
                "name='" + super.getName() + '\'' +
                "; cost=" + super.getCost() +
                "; volume=" + super.getVolume()+
                "; temperature=" + temperature +
                "; id=" + id +
                '}';
    }

     public  boolean contains(Map<String, Object> reference) {
        for (Map.Entry<String, Object> entry : reference.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();

            switch (key) {
                case "name":
                    if(super.getName() != (String) value){
                        return false;
                    }
                    break;
                case "cost":
                    if (super.getCost() != (int) value) {
                        return false;
                    }
                    break;
                case "volume":
                    if (super.getVolume() != (double) value) {
                        return false;
                    }
                    break;
                case "temperature":
                    if (temperature != (int) value) {
                        return false;
                    }
                    break;   
                case "id":
                    if (id != (int) value) {
                        return false;
                    }
                    break;  
                default:
                    return false;
            }
        }

        return true;
    }
}
