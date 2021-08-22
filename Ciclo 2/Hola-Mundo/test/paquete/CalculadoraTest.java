/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package paquete;

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
public class CalculadoraTest {
    
    public CalculadoraTest() {
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
     * Test of suma method, of class Calculadora.
     */
    @Test
    public void testSuma() {
        System.out.println("suma");
        double num1 = 5.0;
        double num2 = 7.0;
        Calculadora instance = new Calculadora();
        double expResult = 12.0;
        double result = instance.suma(num1, num2);
        assertEquals(expResult, result, 0.0);
    }

    /**
     * Test of resta method, of class Calculadora.
     */
    @Test
    public void testSubstraction() {
        System.out.println("resta");
        double num1 = -2.0;
        double num2 = -7.0;
        Calculadora instance = new Calculadora();
        double expResult = 5.0;
        double result = instance.resta(num1, num2);
        assertEquals(expResult, result, 0.0);
    }

    /**
     * Test of multiplicacion method, of class Calculadora.
     */
    @Test
    public void testMultiplication() {
        System.out.println("multiplicacion");
        double num1 = 12.0;
        double num2 = 0.0;
        Calculadora instance = new Calculadora();
        double expResult = 0.0;
        double result = instance.multiplicacion(num1, num2);
        assertEquals(expResult, result, 0.0);
    }

    /**
     * Test of division method, of class Calculadora.
     */
    @Test
    public void testDivisionByNaN() {
        System.out.println("division por NaN");
        double num1 = 0.0;
        double num2 = Double.NaN;
        Calculadora instance = new Calculadora();
        double expResult = Double.NaN;
        double result = instance.division(num1, num2);
        assertEquals(expResult, result, 0.0);
    }
    
    
    @Test
    public void testDivisionByZero() {
        System.out.println("division por cero");
        double num1 = 0.0;
        double num2 = 0.0;
        Calculadora instance = new Calculadora();
        double expResult = Double.NaN;
        double result = instance.division(num1, num2);
        assertEquals(expResult, result, 0.0);
    }
    
    @Test
    public void testDivisionNormal() {
        System.out.println("division");
        double num1 = 3.0;
        double num2 = 2.0;
        Calculadora instance = new Calculadora();
        double expResult = 1.5;
        double result = instance.division(num1, num2);
        assertEquals(expResult, result, 0.1);
    }

    /**
     * Test of main method, of class Calculadora.
     */
    @Test
    public void testMain() {
        System.out.println("main");
        Calculadora.main();
    }
    
}