package CodingTechnique;

import java.util.stream.Stream;

public class StringAndStringBuilder {
    public static void main(String[] args) {
        String string = "abc";
        StringBuilder sb = new StringBuilder("hello");
        StringBuffer sbuf = new StringBuffer("HelloBuffer");


        string += "abc";
        sb.append("abc");
        sbuf.append("abc");

        System.out.println("string = " + string);
        System.out.println("sb = " + sb);
        System.out.println("sbuf = " + sbuf);

        sb.reverse();

        System.out.println("string.toString() = " + string.toString());
        System.out.println("sb.toString() = " + sb.toString());
        System.out.println("sbuf.toString() = " + sbuf.toString());

        StringBuilder stringBuilder = new StringBuilder(string);
        System.out.println("stringBuilder.reverse() = " + stringBuilder.reverse());

        sb.reverse();

    }
}
