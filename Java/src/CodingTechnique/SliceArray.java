package CodingTechnique;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;


public class SliceArray {
    public static void main(String[] args) {
        int[] array = {1,23,4,5,6};
        primitiveSlice(array);
    }
    public static void primitiveSlice(int[] array){
        //slice primitive array to primitive array
        //way1
        int[] ints1 = Arrays.copyOf(array, 2);
        //way2
        int[] ints2 = Arrays.copyOfRange(array, 1, 3);
        System.out.println("Arrays.toString(ints) = " + Arrays.toString(ints2));

        //slice primitive array to List
        List<Integer> collect = Arrays.stream(array).boxed().collect(Collectors.toList()).subList(1,3);
        System.out.println("collect.toString() = " + collect.toString());

        //slice primitive array to Integer Array
        Integer[] integers = Arrays.stream(array).boxed().collect(Collectors.toList()).subList(1, 3).toArray(new Integer[0]);
        System.out.println("integers.toString() = " + Arrays.toString(integers));

    }

}
