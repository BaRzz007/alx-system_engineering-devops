# Install flask from pip3

package { 'flask':
  ensure   => installed,
  name     => 'flask',
  provider => pip3,
#  version  => '2.1.0',
}
