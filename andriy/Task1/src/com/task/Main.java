package com.task;

import java.nio.ByteBuffer;

public class Main {

	public static void main(String[] args) {
		System.out.println(toBinary(add("100", "10"), 15));
	}

	private static double add(String a, String b) {
		return getDecimal(a) + getDecimal(b);
	}

	private static double substract(String a, String b) {
		return getDecimal(a) - getDecimal(b);
	}

	private static double multiply(String a, String b) {
		return getDecimal(a) * getDecimal(b);
	}

	private static double divide(String a, String b) {
		return getDecimal(a) / getDecimal(b);
	}

	private static double getDecimal(String binary) {
		double result;
		try {
			result = Integer.parseInt(binary, 2);
		} catch (NumberFormatException e) {
			result = ByteBuffer.wrap(binary.getBytes()).getDouble();
		}
		return result;

	}

	private static String toBinary(double d, int precision) {
	    long wholePart = (long) d;
	    return wholeToBinary(wholePart) + fractionalToBinary(d - wholePart, precision);
	}

	private static String wholeToBinary(long l) {
	    return Long.toBinaryString(l);
	}

	private static String fractionalToBinary(double num, int precision) {
	    StringBuilder binary = new StringBuilder();
	    while (num > 0 && binary.length() < precision) {
	        double r = num * 2;
	        if (r >= 1) {
	            binary.append(1);
	            num = r - 1;
	        } else {
	            binary.append(0);
	            num = r;
	        }
	    }
	    return binary.toString();
	}
}
