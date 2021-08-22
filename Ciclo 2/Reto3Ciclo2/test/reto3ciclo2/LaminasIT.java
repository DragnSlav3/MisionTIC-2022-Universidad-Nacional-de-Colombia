/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package reto3ciclo2;

import java.util.*;
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author Germán y Lady
 */
public class LaminasIT  {
    
    public LaminasIT() {
    }
    public static void main(String[] args) {
        
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
     * Test of identificarCategorias method, of class Laminas.
     */
    @Test
    public void testIdentificarCategorias() {
        System.out.println("identificarCategorias");
        ArrayList<Integer> listaCategorias= new ArrayList<>();
        listaCategorias.add(1);
        listaCategorias.add(2);
        listaCategorias.add(2);
        listaCategorias.add(2);
        listaCategorias.add(3);
        listaCategorias.add(3);
        listaCategorias.add(1);
        listaCategorias.add(5);
        listaCategorias.add(4);
        listaCategorias.add(7);
        listaCategorias.add(2);
        listaCategorias.add(2);
        listaCategorias.add(2);
        listaCategorias.add(4);
                
        ArrayList<Integer> expResult = new ArrayList<>();
        expResult.add(1);
        expResult.add(2);
        expResult.add(3);
        expResult.add(4);
        expResult.add(5);
        expResult.add(7);
        ArrayList<Integer> result = Laminas.identificarCategorias(listaCategorias);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }

    /**
     * Test of identificarCategoriaLaminasFaltantes method, of class Laminas.
     */
    @Test
    public void testIdentificarCategoriaLaminasFaltantes() {
        System.out.println("identificarCategoriaLaminasFaltantes");
        ArrayList<Integer> listaLaminasFaltantes = null;
        ArrayList<Integer> listaCategorias = null;
        int categoria = 0;
        ArrayList<Integer> expResult = null;
        ArrayList<Integer> result = Laminas.identificarCategoriaLaminasFaltantes(listaLaminasFaltantes, listaCategorias, categoria);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of identificarLaminasRelevantes method, of class Laminas.
     */
    @Test
    public void testIdentificarLaminasRelevantes() {
        System.out.println("identificarLaminasRelevantes");
        ArrayList<Integer> laminasFamilia = null;
        ArrayList<Integer> laminasOtraFamilia = null;
        ArrayList<Integer> expResult = null;
        ArrayList<Integer> result = Laminas.identificarLaminasRelevantes(laminasFamilia, laminasOtraFamilia);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of identificarNumeroLaminasParaCambiar method, of class Laminas.
     */
    @Test
    public void testIdentificarNumeroLaminasParaCambiar() {
        System.out.println("identificarNumeroLaminasParaCambiar");
        ArrayList<Integer> laminasFamilia = null;
        ArrayList<Integer> laminasOtraFamilia = null;
        Integer expResult = null;
        Integer result = Laminas.identificarNumeroLaminasParaCambiar(laminasFamilia, laminasOtraFamilia);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }
    
}
