import yaml


def parse_line(line):
  word_syllables = line.split('=')

  word = word_syllables[0]
  
  syllable_breakdown = word_syllables[1]

  syllables = syllable_breakdown.split('|')
  
  syllable_count_mapping = {'word': word, 'count': len(syllables)}

  return syllable_count_mapping

def parse_file():
  with open('syllables/Syllables.txt') as f:
    with open('syllables/syllables.yaml', 'w') as y:
      lines = f.readlines()

      syllable_counts = [parse_line(line) for line in lines]
      
      yaml.dump(syllable_counts, y)


def prune_file():
  with open('syllables/syllables.yaml', 'r') as r:
    with open('syllables/syllables-pruned.yaml', 'w') as w:
      doc = yaml.load(r)
      pruned = [word for i, word in enumerate(doc) if i % 42 == 0]
      yaml.dump(pruned, w)


parse_file()
prune_file()
