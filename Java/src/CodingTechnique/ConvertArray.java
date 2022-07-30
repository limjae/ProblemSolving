package CodingTechnique;

import java.util.*;
import java.util.stream.Collectors;

public class ConvertArray {
    public static void main(String[] args) {
        int[] array = {1, 23, 4, 5, 6, 1, 2, 23, 5};
        primitiveConvert(array);

        List<Integer> arrayList = new ArrayList<>(Arrays.asList(1, 23, 4, 5, 6, 1, 2, 23, 5));
        listConvert(arrayList);

    }

    public static void primitiveConvert(int[] array) {
        //primitive array to Integer array
        Integer[] integerArray = Arrays.stream(array).boxed().toArray(Integer[]::new);
        System.out.println("integerArray = " + Arrays.toString(integerArray));
        //array to List
        List<Integer> list = Arrays.stream(array).boxed().collect(Collectors.toList());
        System.out.println("list = " + list);
        //array to set
        Set<Integer> set = Arrays.stream(array).boxed().collect(Collectors.toSet());
        System.out.println("set = " + set);
    }

    public static void listConvert(List<Integer> arrayList){
        //List to primitive array
        int[] intArray = arrayList.stream().mapToInt(Integer::intValue).toArray();
        System.out.println("Arrays.toString(intArray) = " + Arrays.toString(intArray));
        //List to integer array
        Integer[] integerArray = arrayList.toArray(Integer[]::new);
        System.out.println("Arrays.toString(integerArray) = " + Arrays.toString(integerArray));
        new HashSet<>(arrayList);
    }
}
