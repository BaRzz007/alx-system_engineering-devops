# Install flask from pip3

package { 'flask==2.1.0':
  path	=> ['/usr/bin', '/bin', '/usr/sbin']
  ensure   => installed,
  name     => 'flask',
  provider => 'pip3'
}
