# tester	test_sequence	test_score
# Alice		    1		        10
# Alice		    2		        10
# Alice		    3		        Null
# Alice		    4		        20
# Alice		    5		        15
# Alice		    6		        Null
# Bob		    1		        21
# Bob		    2		        Null
# Bob		    3		        Null
# Bob		    4		        Null
# Bob		    5		        15
# Bob		    6		        9
# Dave		    1		        22
# Dave		    2		        23
# Dave		    3		        Null
# Dave		    4		        Null
# Dave		    5		        Null
# Dave		    6		        Null
# Rick		    1		        32
# Rick		    2		        Null
# Rick		    3		        36
# Rick		    4		        Null
# Rick		    5		        Null
# Rick		    6		        27

import pandas as pd
import numpy as np

data = {
    'tester': ['Alice', 'Alice', 'Alice', 'Alice', 'Alice', 'Alice',
               'Bob', 'Bob', 'Bob', 'Bob', 'Bob', 'Bob',
               'Dave', 'Dave', 'Dave', 'Dave', 'Dave', 'Dave',
               'Rick', 'Rick', 'Rick', 'Rick', 'Rick', 'Rick'],
    'test_sequence': [1, 2, 3, 4, 5, 6,
                      1, 2, 3, 4, 5, 6,
                      1, 2, 3, 4, 5, 6,
                      1, 2, 3, 4, 5, 6],
    'test_score': [10, 10, np.nan, 20, 15, np.nan,
                   21, np.nan, np.nan, np.nan, 15, 9,
                   22, 23, np.nan, np.nan, np.nan, np.nan,
                   32, np.nan, 36, np.nan, np.nan, 27]
}

df = pd.DataFrame(data)

df['test_score'] = df.groupby('tester')['test_score'].ffill()

print(df)
