package CodingTechnique;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ConvertType {
    public static void main(String[] args) {


    }

    public void stringToValue(){
        String s = "21";
        Integer i1  = Integer.parseInt(s); // int
        Integer i2  = Integer.valueOf(s); //Integer
        Long l1 = Long.parseLong(s); // long
        Long l2 = Long.valueOf(s);
        Double d1 = Double.parseDouble(s);
        Double d2 = Double.valueOf(s);
    }

    public void valueToString(){

    }

}
