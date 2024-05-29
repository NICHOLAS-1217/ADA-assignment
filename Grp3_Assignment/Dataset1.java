import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;

public class Dataset1 {

    public static void main(String[] args) {
        long groupLeaderId = 1211103412L; // Group leader's ID
        int[] sizes = { 100, 1000, 10000, 100000, 500000, 1000000 };// Sizes of the datasets

        // Generate datasets
        for (int i = 0; i < sizes.length; i++) {
            generateDataset(groupLeaderId, sizes[i], "Dataset1_Set" + (i + 1) + ".txt");
        }

        System.out.println("Datasets generated and saved to text files.");
    }

    // Generates a dataset of the specified size using the given seed and writes it to a file.
    private static void generateDataset(long seed, int size, String fileName) {
        // Extract digits from the seed
        List<Integer> digits = extractDigits(seed);
        Random random = new Random(seed);

        try (FileWriter writer = new FileWriter(fileName)) {
            for (int j = 0; j < size; j++) {
                // Select a random digit from the list of digits
                int number = generateNumberUsingDigits(random, digits);
                writer.write(number + "\n"); // Write the generated number to the file
            }
        } catch (IOException e) {
            System.err.println("Error writing to file: " + fileName);
            e.printStackTrace();
        }
    }

    private static List<Integer> extractDigits(long number) {
        Set<Integer> digitSet = new HashSet<>();
        while (number > 0) {
            digitSet.add((int) (number % 10)); // Extract the last digit and add it to the set
            number /= 10; // Remove the last digit
        }
        return new ArrayList<>(digitSet); //Convert the set to list
    }

    private static int generateNumberUsingDigits(Random random, List<Integer> digits) {
        int length = random.nextInt(3) + 1; // Random length between 1 and 3 digits
        int number = 0;
        for (int i = 0; i < length; i++) {
            number = number * 10 + digits.get(random.nextInt(digits.size()));
        }
        return number;
    }
}
