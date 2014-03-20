// import java.util.*;
// import java.io.*;

public class Main {
	public static void main(String[] args) {
		int[] numbers = {1, 2, 3};
		int length = numbers.length;
		char[] chars = new char[length];

		for (int i = 0; i < chars.length; i++)		chars[i] = (char)(i + 65);
		
		for (char c : chars)		System.out.println(c);

		Point p = new Point(3, 4);  // class Point defined in Point.java
		p.print();
	}

}