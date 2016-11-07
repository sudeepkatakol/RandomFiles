package package1;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/")
public class View extends HttpServlet{
    
    Controller controller;
    public View() {
        super();  
    }
    private static final long serialVersionUID = 1L;
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        PrintWriter out = response.getWriter();
        try {
            controller = new Controller();
            List<HashMap<String, String>> results = controller.getData();
            out.println("<table>");
            out.println("<tr>");
            out.println("<th> NAME </th>");
            out.println("<th> BIO </th>");
            out.println("<th> EMAIL </th>");
            out.println("</tr>");
            for(HashMap<String, String> map : results) {
                out.println("<tr>");
                out.println("<td>" + map.get("name") +"</td>");
                out.println("<td>" + map.get("bio") +"</td>");
                out.println("<td>" + map.get("email") +"</td>");
                out.println("</tr>");
            }
            out.println("<table>");
        } catch (Exception e) {
            e.printStackTrace(out);
        }
    }
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        doGet(request, response);
        
    }
}
