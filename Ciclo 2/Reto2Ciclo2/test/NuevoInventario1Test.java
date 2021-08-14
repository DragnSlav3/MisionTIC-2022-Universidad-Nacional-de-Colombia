/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author Germán y Lady
 */
public class NuevoInventario1Test {
    
    public NuevoInventario1Test() {
    }
    
    @BeforeAll
    public static void setUpClass() {
    }
    
    @AfterAll
    public static void tearDownClass() {
    }
    
    @BeforeEach
    public void setUp() {
    }
    
    @AfterEach
    public void tearDown() {
    }

    /**
     * Test of adicionarComputador method, of class NuevoInventario1.
     */
    @Test
    public void testAdicionarComputador() {
        System.out.println("adicionarComputador");
        NuevoInventario1.adicionarComputador();
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }

    /**
     * Test of listarComputadores method, of class NuevoInventario1.
     */
    @Test
    public void testListarComputadores() {
        System.out.println("listarComputadores");
        NuevoInventario1.listarComputadores();
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }

    /**
     * Test of procesarComandos method, of class NuevoInventario1.
     */
    @Test
    public void testProcesarComandos() {
        System.out.println("procesarComandos");
        NuevoInventario1.procesarComandos();
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }

    /**
     * Test of main method, of class NuevoInventario1.
     */
    @Test
    public void testMain() {
        System.out.println("main");
        String[] args = null;
        NuevoInventario1.main(args);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    
}
