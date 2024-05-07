import java.util.*;

public class word_count_11 {
    public static void main(String[] args) {
        String paragraph = "This is a sample paragraph with several words. " +
                            "We will count the number of words in this paragraph.";

        // Split the paragraph into words using space as delimiter
        String[] words = paragraph.split("\\s+");

        // Count the number of words
        int wordCount = words.length;

        System.out.println("Number of words in the paragraph: " + wordCount);
    }
}
