package package1;

import java.util.HashMap;
import java.util.List;

public class View2 {
   
    public static void main(String[] args) {
        Controller controller;
        try {
            controller = new Controller();
            List<HashMap<String, String>> results = controller.getData();
            for(HashMap<String, String> map : results) {
                System.out.println(map.get("name") );
                System.out.println(map.get("bio"));
                System.out.println(map.get("email"));
            }
        } catch (Exception e) {
           e.printStackTrace();
        }
    }
    
}
