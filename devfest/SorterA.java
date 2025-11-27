package devfest;

import java.util.ArrayList;
import java.util.List;

public class SorterA<T extends Comparable<T>> {

	private final List<T> array;

	private SorterA(List<T> values) {
		this.array = new ArrayList<>(values);
	}

	public static <T extends Comparable<T>>
	List<T> sort(RandomlyFilled<T> input) {
		if (input.size() <= 1) {
			return input.values();
		}
		var s = new SorterA<>(input.values());
		s.qsort(0, input.size() - 1);
		return List.copyOf(s.array);
	}

	private void qsort(int lo, int hi) {
		if (lo < hi) {
			int pivotIndex = partition(lo, hi);
			qsort(lo, pivotIndex - 1);
			qsort(pivotIndex + 1, hi);
		}
	}

	private int partition(int lo, int hi) {
		T pivot = array.get(hi);
		int i = lo - 1;
		for (int j = lo; j < hi; j++) {
			if (array.get(j).compareTo(pivot) <= 0) {
				i++;
				swap(i, j);
			}
		}
		swap(i + 1, hi);
		return i + 1;
	}

	private void swap(int i, int j) {
		T temp = array.get(i);
		array.set(i, array.get(j));
		array.set(j, temp);
	}
}
