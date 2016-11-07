package package1;

import java.util.List;

import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.Row;
import com.datastax.driver.core.Session;

public class Model {
    Cluster cluster;
    Session session;
    
    class DatabaseException extends Exception {
        
        private static final long serialVersionUID = 1L;

        public DatabaseException() {
            super("Couldn't connect to database \n");
        }
    }
    
    public Model() throws Exception {
        cluster = Cluster.builder().addContactPoint("127.0.0.1").build();
        try {
        session = cluster.connect();
        useKeyspace();
        } catch (Exception e) {
            throw new DatabaseException();
        }
            
    }
    
    public void useKeyspace() throws Exception {
        try {
        String query = "use random";
        session.execute(query);
        } catch (Exception e) {
            throw new DatabaseException();
        }
    }
    
    public List<Row> getData() throws Exception {
        try {
            String query = "SELECT * FROM data;";
            return session.execute(query).all();
            } catch (Exception e) {
                throw new DatabaseException();
            }
    }
}
