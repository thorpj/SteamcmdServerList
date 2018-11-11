
lib = File.expand_path("../lib", __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require "steamcmd_server_list"

Gem::Specification.new do |spec|
  spec.name          = "steamcmd_server_list"
#  spec.version       = steamcmd_server_list::VERSION
  spec.authors       = ["Joe Thorpe"]
  spec.email         = ["thorpejoe4@gmail.com"]

  spec.summary       = %q{Scrapes Steam Dedicated Server list}
  # spec.homepage      = "TODO: Put your gem's website or public repo URL here."

  # Prevent pushing this gem to RubyGems.org. To allow pushes either set the 'allowed_push_host'
  # to allow pushing to a single host or delete this section to allow pushing to any host.
  if spec.respond_to?(:metadata)
    spec.metadata["allowed_push_host"] = "TODO: Set to 'http://mygemserver.com'"
  else
    raise "RubyGems 2.0 or newer is required to protect against " \
      "public gem pushes."
  end

  # Specify which files should be added to the gem when it is released.
  # The `git ls-files -z` loads the files in the RubyGem that have been added into git.
  spec.files         = Dir.chdir(File.expand_path('..', __FILE__)) do
    `git ls-files -z`.split("\x0").reject { |f| f.match(%r{^(test|spec|features)/}) }
  end
  spec.bindir        = "exe"
  spec.executables   = spec.files.grep(%r{^exe/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]

  #spec.add_development_dependency "bundler", "~> 1.16"
  #spec.add_development_dependency "rake", "~> 10.0"
  #spec.add_development_dependency "rspec", "~> 3.7.0"
  #spec.add_development_dependency "httparty", "~> 0.16.2"

  #spec.add_development_dependency "minitest"
  #spec.add_development_dependency "vcr"
  #spec.add_development_dependency "webmock"
  #spec.add_development_dependency "faraday"

  #spec.add_dependency "httparty", "~> 0.16.2"
  #spec.add_dependency "activesupport", "~> 5.2"
  #spec.add_dependency "active_attr", "~> 0.11.0"
end
