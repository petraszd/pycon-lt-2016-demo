(func fibonacci-numbers (n)
      (func iter (a b n)
            (if (< n 0)
              a
              ((display b)
               (iter b (+ a b) (- n 1)))))
      (iter 0 1 (- n 1)))

(fibonacci-numbers 10)
