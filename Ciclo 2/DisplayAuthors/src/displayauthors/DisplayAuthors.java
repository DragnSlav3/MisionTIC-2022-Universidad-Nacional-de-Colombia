/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package displayauthors;
import java.sql.Connection;
import java.sql.Statement;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;

public class DisplayAuthors 
{
   // nombre del controlador de JDBC y URL de la base de datos                              
   static final String DATABASE_URL = "jdbc:mysql://localhost/books";
   
   // inicia la aplicación
   public static void main( String args[] )
   {
      Connection connection = null; // manages connection
      Statement statement = null; // query statement
      ResultSet resultSet = null; // manages results
    
      // se conecta a la base de datos libros
      try 
      {
         // establece la conexión a la base de datos
         connection = DriverManager.getConnection( 
            DATABASE_URL, "root", "80156436" );

         // crea objeto Statement para consultar la base de datos
         statement = connection.createStatement();
         
         // consulta la base de datos                                       
         resultSet = statement.executeQuery(            
            "SELECT authorID, firstName, lastName FROM authors" );
         
         // procesa los resultados de la consulta
         ResultSetMetaData metaData = resultSet.getMetaData();
         int numberOfColumns = metaData.getColumnCount();     
         System.out.println( "Authors Table of Books Database:\n" );
         
         for ( int i = 1; i <= numberOfColumns; i++ )
            System.out.printf( "%-8s\t", metaData.getColumnName( i ) );
         System.out.println();
         
         while ( resultSet.next() ) 
         {
            for ( int i = 1; i <= numberOfColumns; i++ )
               System.out.printf( "%-8s\t", resultSet.getObject( i ) );
            System.out.println();
         } // fin while
      }  // fin try
      catch ( SQLException sqlException )                                
      {                                                                  
         sqlException.printStackTrace();
      } // fin catch                                                     
      finally // asegura que conjuntoResultados, instruccion y conexion estén cerrados
      {                                                             
         try                                                        
         {                                                          
            resultSet.close();                                      
            statement.close();                                      
            connection.close();                                     
         } // fin try                                               
         catch ( Exception exception )                              
         {                                                          
            exception.printStackTrace();                            
         } // fin catch                                             
      } // fin finally                                              
   } // fin main
} // fin clase DisplayAuthors