package devfest;

import java.util.List;

import static java.lang.reflect.Array.newInstance;

public class SorterB<T extends Comparable<T>> {
    private final T[] array;

    @SuppressWarnings("unchecked")
    private SorterB(List<T> unordered) {
        this.array = unordered.toArray(len ->
            (T[]) newInstance(array.type(), len)
        );
    }

    public static <T extends Comparable<T>>
	List<T> sort(RandomlyFilled<T> input) {
        if (input.size() <= 1) {
            return input.values();
        }
        var sorter = new SorterB<>(input.values());
        sorter.qsort(0, input.size() - 1);
        return List.of(sorter.array);
    }

    private void qsort(int lo, int hi) {
        if (lo < hi) {
            int cut = hoarePartition(lo, hi);
            qsort(lo, cut); // Hoare => include pivot
            qsort(cut + 1, hi);
        }
    }

    private int hoarePartition(int lo, int hi) {
        T pivot = array[lo];

        for (int left = lo - 1, right = hi + 1;;) {
            do ++left;
            while (array[left].compareTo(pivot) < 0);
            do --right;
            while (array[right].compareTo(pivot) > 0);

            if (left >= right) {
                return right;
            }
            swap(left, right);
        }
    }

    private void swap(int i, int j) {
        T temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
