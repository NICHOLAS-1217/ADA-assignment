import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

class Star {
	String name;
	int x;
	int y;
	int z;
	int weight;
	int profit;

    // Constructor to initialize the Star object
	public Star(String name, int x, int y, int z, int weight, int profit) {
		this.name = name;
		this.x = x;
		this.y = y;
		this.z = z;
		this.weight = weight;
		this.profit = profit;
	}

    // String representation of the Star object
	@Override
	public String toString() {
		return name + " " + x + " " + y + " " + z + " " + weight + " " + profit;
	}
}

public class Dataset2 {
	private static final int NUMBER_OF_STARS = 20; // Number of stars to generate

	public static void main(String[] args) throws IOException {
		long seed = 3633314718L; //Sum of other group members’ ID number 
		List<Integer> digits = extractDigits(seed); // Extract digits from the seed
		Random random = new Random(seed); // Initialize Random object with the seed

        // List to store the generated stars
		List<Star> stars = new ArrayList<>();
		for (int i = 0; i < NUMBER_OF_STARS; i++) {
			String name = "Star " + (char) ('A' + i); // Generate star name (Star A, Star B, ...)
			int x = generateNumberUsingDigits(random, digits); // Generate random x coordinate
			int y = generateNumberUsingDigits(random, digits); // Generate random y coordinate
			int z = generateNumberUsingDigits(random, digits); // Generate random z coordinate
			int weight = generateNumberUsingDigits(random, digits, 2); // Generate random weight
			int profit = generateNumberUsingDigits(random, digits, 2); // Generate random profit
			stars.add(new Star(name, x, y, z, weight, profit)); // Add star to the list
		}
        // Save the generated data to a file
		saveStarsDataToFile(stars);
	}

    // Extract digits from the given number and return as a list
	private static List<Integer> extractDigits(long number) {
		Set<Integer> digitSet = new HashSet<>(); //Use a set to store unique digits
		while (number > 0) {
			digitSet.add((int) (number % 10)); // Extract the last digit and add to the set
			number /= 10; // Remove the last digit from the number
		}
		return new ArrayList<>(digitSet); // Convert the set to a list
	}

    // Generate a random number using the extracted digits for weight
	private static int generateNumberUsingDigits(Random random, List<Integer> digits) {
		int length = random.nextInt(3) + 1; // Random length between 1 and 3 digits
		int number = 0;
		for (int i = 0; i < length; i++) {
			number = number * 10 + digits.get(random.nextInt(digits.size())); // Add random digit to numbe
		}
		return number;
	}

    // Generate a random number using the extracted digits for profit
	private static int generateNumberUsingDigits(Random random, List<Integer> digits, int numDig) {
		int length = random.nextInt(numDig) + 1; // Random length between 1 and numDig digits
		int number = 0;
		for (int i = 0; i < length; i++) {
			number = number * 10 + digits.get(random.nextInt(digits.size())); // Add random digit to number
		}
		return number;
	}

	// Save the star data to a file
    private static void saveStarsDataToFile(List<Star> stars) throws IOException {
        try (FileWriter writer = new FileWriter("Dataset2.txt")) {
            for (Star star : stars) {
                writer.write(star.toString() + "\n"); // Write each star's data to the file
            }
            System.out.println("Star data generated and saved to Dataset2.txt.");
        }
    }
}


