## ADDED Requirements

### Requirement: Music and navigation retain independent state

DiPlay SHALL process music, navigation and lane state through their respective owners. Ending or pausing one domain MUST NOT clear valid state belonging to another domain.

#### Scenario: Music is paused while navigation remains active
- **WHEN** a 5001 pause update arrives while valid route guidance remains active
- **THEN** the music state SHALL reflect the update
- **AND** route/maneuver/lane state SHALL remain governed by navigation updates and its own lifecycle

#### Scenario: Navigation ends while music keeps playing
- **WHEN** valid route termination is received with unchanged active music
- **THEN** navigation outputs SHALL follow their documented clear policy
- **AND** music state SHALL remain unchanged

### Requirement: Playback consumers preserve explicit state semantics

Playback consumers SHALL retain or interpret actual wire states according to a documented consumer purpose. PLAYING, PAUSED, STOPPED, seek states and unknown values MUST have tested behavior; divergent booleans SHALL be resolved through that model rather than assumed equivalent.

#### Scenario: The wire reports seeking
- **WHEN** a valid seeking state is received
- **THEN** the playback model and each affected consumer SHALL follow its documented behavior
- **AND** tests SHALL verify both the media consumer and cluster-song consumer

### Requirement: Output callbacks respect owner replacement

Receiver output workers SHALL prevent callbacks belonging to an ended owner from changing replacement outputs. Overflow, blocking vendor work and repeated cleanup SHALL have a defined state/clear policy. Retained presentation MUST have a documented validity/expiry boundary.

#### Scenario: A vendor call finishes after replacement
- **WHEN** an old owner's vendor call finishes after a replacement owner starts
- **THEN** subsequent stale output work SHALL NOT update or clear the replacement owner's display state

### Requirement: Interoperability results remain reproducible and bounded

Source interoperability tests SHALL record both commits and hashes of the actual parser inputs. Receiver source MUST remain outside production compilation. Transport completion, parser acceptance and real display observations SHALL be reported separately.

#### Scenario: Parser tests pass without a vehicle run
- **WHEN** actual DiPlay parser tests pass but no matching vehicle observation exists
- **THEN** results SHALL report local parser success only
- **AND** the real display acceptance task SHALL remain incomplete
