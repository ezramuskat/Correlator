import pandas as pd
import sys
import collections




def findCorrelations(frame: pd.DataFrame, significance: int) -> pd.DataFrame:
	return frame.corr('pearson', significance, True)

def getSignificantCorrelations(frame: pd.DataFrame):
	correlatedFrame = findCorrelations(frame, 1)
	correlatedFrame.columns = correlatedFrame.columns.str.replace(r'\s+', '_')
	correlatedFrame.index = correlatedFrame.index.str.replace(r'\s+', '_')
	returnList: list[tuple[str,str,float]] = []
	for row in correlatedFrame.itertuples():
		index:str = row[0]
		for column, value in zip(row._fields, row):
			if column == "Index" or column == index:
				continue
			cell_value = pd.to_numeric(value)
			if abs(cell_value) > 0.5:
				returnList.append((index, column, cell_value))
	return returnList

def findClusters(frame: pd.DataFrame, significance: int):
	return 1

if __name__ == "__main__":
	frame = pd.read_excel(sys.argv[1])
	print(findCorrelations(frame, 1))
	print(getSignificantCorrelations(frame))
