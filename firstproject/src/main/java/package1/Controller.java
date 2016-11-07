package package1;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import com.datastax.driver.core.Row;

public class Controller {
    
    private Model model;
    
    public Controller() throws Exception {
        model = new Model(); 
    }
    
    public List<HashMap<String, String>> getData() throws Exception {
        List<Row> result = model.getData();
        List<HashMap<String, String>> data = new ArrayList<HashMap<String, String>>();
        HashMap<String, String> mapRow = new HashMap<String, String>();
        for(Row row : result) {
            mapRow.clear();
            mapRow.put("name", row.getString("name"));
            mapRow.put("bio", row.getString("bio"));
            mapRow.put("email", row.getString("email"));
            data.add(mapRow);
        }
        return data;
    }
    
}
